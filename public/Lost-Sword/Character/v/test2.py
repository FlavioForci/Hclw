from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import time

def scrape_and_save_titles(url, filename="titles.txt"):
    """
    Ruft chinesische Titel von einer Webseite ab und speichert sie in einer Textdatei.

    Args:
        url (str): Die URL der Webseite.
        filename (str): Der Name der Datei, in der die Titel gespeichert werden sollen.
    """
    try:
        service = Service('./chromedriver.exe')  # Ersetzen Sie dies durch den Pfad zu Ihrem ChromeDriver
        driver = webdriver.Chrome(service=service)
        driver.get(url)
        time.sleep(5)  # Warte, bis die Seite geladen ist.

        soup = BeautifulSoup(driver.page_source, "html.parser")
        items = soup.find_all("a", class_="item", attrs={"data-v-0a523baa": ""})

        with open(filename, "w", encoding="utf-8") as f:
            for item in items:
                title = item.get("title")
                if title:
                    f.write(title + "\n")

        print(f"Titel wurden erfolgreich in '{filename}' gespeichert.")
        driver.quit()

    except Exception as e:
        print(f"Ein Fehler ist aufgetreten: {e}")
        try:
            driver.quit()
        except:
            pass

url = "https://www.gamekee.com/lostsword/"
scrape_and_save_titles(url)