import os
import csv
import requests
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup
from collections import deque

class AdvancedLinkChecker:
    def __init__(self, base_url, user_agent=None):
        self.base_url = base_url
        self.domain = urlparse(base_url).netloc
        self.visited = set()
        self.queue = deque()
        self.broken_links = []
        self.headers = {'User-Agent': user_agent or 'Mozilla/5.0 (compatible; LinkChecker/2.0)'}
        self.queue.append(base_url)

    def is_internal(self, url):
        return urlparse(url).netloc == self.domain

    def check_response(self, url, source):
        try:
            response = requests.head(url, 
                                   headers=self.headers, 
                                   allow_redirects=True, 
                                   timeout=15,
                                   verify=True)
            
            if 400 <= response.status_code < 500:
                self.broken_links.append({
                    'source': source,
                    'target': response.url,
                    'status': response.status_code,
                    'redirects': [r.url for r in response.history]
                })
                return False
            return True
        except Exception as e:
            print(f"Fehler: {str(e)}")
            return False

    def crawl_site(self):
        while self.queue:
            current_url = self.queue.popleft()
            
            if current_url in self.visited:
                continue
                
            self.visited.add(current_url)
            print(f"Prüfe: {current_url}")

            try:
                response = requests.get(current_url, 
                                      headers=self.headers, 
                                      timeout=15,
                                      verify=True)
                soup = BeautifulSoup(response.text, 'html.parser')

                for link in soup.find_all(['a', 'img', 'link', 'script']):
                    href = link.get('href') or link.get('src')
                    if not href:
                        continue

                    absolute_url = urljoin(current_url, href)
                    parsed = urlparse(absolute_url)
                    
                    # Filtere unerwünschte URLs
                    if parsed.scheme not in ('http', 'https'):
                        continue
                    if not self.is_internal(absolute_url):
                        continue
                    if any(ext in absolute_url for ext in ['.pdf', '.jpg', '.png']):
                        continue

                    # Füge neue URLs zur Warteschlange hinzu
                    if absolute_url not in self.visited and absolute_url not in self.queue:
                        self.queue.append(absolute_url)

                    # Prüfe den Link
                    self.check_response(absolute_url, current_url)
                    
                

            except Exception as e:
                print(f"Fehler beim Crawlen von {current_url}: {str(e)}")

    def generate_report(self):
        with open('full_crawl_report.csv', 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['Quellseite', 'Defekter Link', 'Statuscode', 'Redirect-Pfad'])
            
            for entry in self.broken_links:
                writer.writerow([
                    entry['source'],
                    entry['target'],
                    entry['status'],
                    ' → '.join(entry['redirects'])
                ])

        print(f"\nCrawling-Statistik:")
        print(f"Geprüfte Seiten: {len(self.visited)}")
        print(f"Gefundene 4XX-Links: {len(self.broken_links)}")
        print(f"Report-Datei: full_crawl_report.csv")

if __name__ == "__main__":
    checker = AdvancedLinkChecker(
        base_url="https://tychara.com",  # URL anpassen
        user_agent="Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
    )
    checker.crawl_site()
    checker.generate_report()
