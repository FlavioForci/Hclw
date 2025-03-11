import os
from bs4 import BeautifulSoup

def generate_description(soup):
    """Generiert eine SEO-optimierte Description"""
    title = soup.title.string.strip() if soup.title else ""
    first_paragraph = soup.find('p').get_text().strip()[:120] if soup.find('p') else ""
    
    # Kombiniere Title + ersten Satz des Contents
    return f"{title} - {first_paragraph}... | Professionelle Webseite".strip()

def update_descriptions(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".html"):
                filepath = os.path.join(root, file)
                
                with open(filepath, 'r+', encoding='utf-8') as f:
                    soup = BeautifulSoup(f.read(), 'html.parser')
                    
                    # Finde/Erstelle Meta-Description
                    meta = soup.find('meta', attrs={'name': 'description'})
                    new_description = generate_description(soup)
                    
                    if meta:
                        meta['content'] = new_description
                    else:
                        new_tag = soup.new_tag('meta', attrs={'name': 'description', 'content': new_description})
                        soup.head.append(new_tag)
                    
                    # Datei überschreiben
                    f.seek(0)
                    f.write(str(soup))
                    f.truncate()
                print(f"Updated: {filepath}")

if __name__ == "__main__":
    folder = input("Pfad zum HTML-Ordner: ")
    update_descriptions(folder)
