import os
import re
import chardet
from pathlib import Path
from bs4 import BeautifulSoup
from collections import defaultdict

class TitleOptimizer:
    def __init__(self, base_dir):
        self.base_dir = base_dir
        self.title_registry = defaultdict(list)
        self.log = []

    def detect_encoding(self, filepath):
        with open(filepath, 'rb') as f:
            rawdata = f.read()
            result = chardet.detect(rawdata)
            return result['encoding']

    def read_file(self, filepath):
        try:
            encoding = self.detect_encoding(filepath)
            with open(filepath, 'r', encoding=encoding, errors='replace') as f:
                return f.read()
        except Exception as e:
            print(f"Error reading {filepath}: {str(e)}")
            return None

    def analyze_existing_title(self, title, filepath):
        if not title:
            return False, "Missing title"
            
        issues = []
        if len(title) > 60:
            issues.append(f"Too long ({len(title)} chars)")
        if title.lower() in ['untitled document', 'new page']:
            issues.append("Generic title")
        if re.search(r"[^\x00-\x7F]", title):
            issues.append("Non-ASCII characters")
        if len(issues) > 0:
            return False, ", ".join(issues)
        return True, "OK"

    def generate_new_title(self, soup, filepath):
        h1 = soup.find('h1')
        h1_text = h1.get_text(strip=True) if h1 else ""
        
        meta_desc = soup.find('meta', attrs={'name': 'description'})
        meta_text = (meta_desc['content'].strip()[:65] 
                    if meta_desc and meta_desc.get('content') else "")

        path_parts = [p for p in Path(filepath).parts if p not in ('', '.')]
        path_keywords = ' '.join(path_parts[-2:]).replace('-', ' ').title()

        components = [
            h1_text,
            meta_text,
            path_keywords,
            "Content Page"
        ]

        primary = next((c for c in components if len(c) > 3), "Content Page")
        title = re.sub(r'\s+', ' ', primary).strip()
        return self.make_unique(title[:65].strip(), filepath)

    def make_unique(self, title, filepath):
        base_title = title
        counter = 2
        while base_title in self.title_registry:
            base_title = f"{title} ({counter})"
            counter += 1
        self.title_registry[base_title].append(filepath)
        return base_title

    def process_file(self, filepath):
        content = self.read_file(filepath)
        if not content:
            return

        soup = BeautifulSoup(content, 'html.parser')
        original_title = soup.title.string if soup.title else ""

        is_valid, reason = self.analyze_existing_title(original_title, filepath)
        
        if not is_valid:
            new_title = self.generate_new_title(soup, filepath)
            
            if not soup.title:
                soup.head.append(soup.new_tag('title'))
            
            soup.title.string = new_title
            
            try:
                encoding = self.detect_encoding(filepath)
                with open(filepath, 'w', encoding=encoding, errors='replace') as f:
                    f.write(str(soup))
            except Exception as e:
                print(f"Error writing {filepath}: {str(e)}")
                return

            self.log.append({
                'file': filepath,
                'original': original_title,
                'new': new_title,
                'reason': reason
            })

    def run(self, dry_run=False):
        for root, _, files in os.walk(self.base_dir):
            for file in files:
                if file.endswith('.html'):
                    filepath = os.path.join(root, file)
                    if dry_run:
                        self.analyze_only(filepath)
                    else:
                        self.process_file(filepath)

        self.generate_report()

    def analyze_only(self, filepath):
        content = self.read_file(filepath)
        if not content:
            return

        soup = BeautifulSoup(content, 'html.parser')
        original_title = soup.title.string if soup.title else ""
        
        is_valid, reason = self.analyze_existing_title(original_title, filepath)
        if not is_valid:
            new_title = self.generate_new_title(soup, filepath)
            self.log.append({
                'file': filepath,
                'original': original_title,
                'new': new_title,
                'reason': reason
            })

    def generate_report(self):
        print("\nSEO Title Optimization Report:")
        print(f"{'File':<40} | {'Original Title':<50} | {'New Title':<50} | Issues")
        print('-' * 160)
        for entry in self.log:
            print(f"{entry['file'][-40:]:<40} | {entry['original'][:45]:<50} | {entry['new'][:45]:<50} | {entry['reason']}")

if __name__ == "__main__":
    optimizer = TitleOptimizer(
        base_dir='C:/Users/flavi/Desktop/Hclw/public'  # Set your website path here
    )
    print("Running dry-run...")
    optimizer.run(dry_run=True)
    
    # Uncomment to apply changes after verifying
    # print("\nApplying changes...")
    # optimizer.run(dry_run=False)
