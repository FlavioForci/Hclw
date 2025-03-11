import os
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from multiprocessing import Pool

# Pfad zum WebDriver
webdriver_path = r'./chromedriver.exe'

# Liste von URLs von 645900 bis 646950
urls = [f'https://www.gamekee.com/lostsword/{i}.html' for i in range(645900, 646950)]

# Ordner, in dem die Bilder gespeichert werden sollen
output_folder = 'bilder_gamekee'

# Wenn der Ordner nicht existiert, erstelle ihn
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Chinesisch-Englisch Namensübersetzungen
name_translations = {
    '莉莎': 'Lisa',
    '加拉哈德': 'Galahad',
    '伊丽莎白': 'Elizabeth',
    '维维安': 'Vivian',
    '特里斯坦': 'Tristan',
    '莉亚': 'Ria',
    '兰恩': 'Ran',
    '帕西瓦尔': 'Percival',
    '摩尔加兹': 'Morgause',
    '莫甘娜': 'Morgana',
    '米娅': 'Mia',
    '梅林': 'Merlin',
    '露西': 'Lucy',
    '鲁亚': 'Lua',
    '莉莉丝': 'Lilith',
    '瑟茜': 'Circe',
    '凯伊': 'Kay',
    '卡特琳': 'Catherine',
    '圣女贞德': 'Joan-of-Arc',
    '伊索尔德': 'Isolde',
    '伊莎贝尔': 'Isabelle',
    '桂妮维亚': 'Guinevere',
    '加文': 'Gawain',
    '恩雅': 'Enya',
    '艾娃': 'Ava',
    '提亚玛特': 'Tiamat',
    '阿莲': 'Alen',
    '莫德雷德': 'Mordred',
    '兰斯洛特': 'Lancelot',
    '克里斯蒂娜': 'Christina',
    '克莱尔': 'Claire',
    '艾丹': 'Aidan',
    '贝迪维尔': 'Bedivere',
    '乌利恩': 'Urien',
    '萨拉': 'Sarah',
    '雷伊': 'Ray',
    '妮妙': 'Nymue',
    '梅里': 'Meri',
    '罗安娜': 'Roanna',
    '加赫里斯': 'Gaheris',
    '艾斯梅拉达': 'Esmeralda',
    '贝林': 'Baylin',
    '艾莲': 'Aileen',
    '丽塔': 'Rita',
    '瑞秋': 'Rachel',
    '杰西': 'Jessie',
    '艾琳': 'Eileen',
    '伊希斯': 'Isis'
}

# Funktion zum Downloaden der Bilder für eine einzelne URL
def download_images(url):
    options = Options()
    options.add_argument('--headless')  # Headless-Modus aktivieren
    prefs = {"profile.managed_default_content_settings.images": 2} #Bilder blockieren
    options.add_experimental_option("prefs", prefs)
    service = Service(webdriver_path)
    driver = webdriver.Chrome(service=service, options=options)
    driver.get(url)

    try:
        # Name des Charakters extrahieren (mit explizitem Wait)
        name_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'h1.title'))
        )

        name_chinese = name_element.text.strip()
        name = name_translations.get(name_chinese, name_chinese) # Benutze englische Version, wenn vorhanden

        if name_chinese not in name_translations: # Wenn der Name nicht in der Uebersetzungs tabelle ist, ignoriere diese URL.
          print(f"Name {name_chinese} nicht in Liste. Ignoriere {url}")
          driver.quit()
          return

    except TimeoutException:
        print(f"Element nicht gefunden auf {url}")
        driver.quit()
        return
    except Exception as e:
        print(f"Fehler beim Extrahieren des Namens von {url}: {e}")
        driver.quit()
        return

    # CSS-Selektoren für die Bilder
    css_selectors = [
        'img[src*="cdnimg-v2.gamekee.com"]',
        'img[src*="images/w_85"]',
        'img[src*="images/w_86"]'
    ]

    count = 0
    session = requests.Session() # Session wiederverwendung
    for selector in css_selectors:
        img_tags = driver.find_elements(By.CSS_SELECTOR, selector)

        for index, img_tag in enumerate(img_tags):
            if count >= 8:
                break

            img_url = img_tag.get_attribute('src')

            # Wenn die URL mit '//' beginnt, füge 'https:' hinzu
            if img_url.startswith('//'):
                img_url = 'https:' + img_url

            # Bild herunterladen
            try:
                response = session.get(img_url) # Session anstelle von requests.get()
                # Überprüfen, ob die Anfrage erfolgreich war
                if response.status_code == 200:
                    # Bild speichern
                    img_name = f'{name}Skill{count + 1}.png'
                    with open(os.path.join(output_folder, img_name), 'wb') as file:
                        file.write(response.content)
                    print(f'{img_name} erfolgreich heruntergeladen!')
                    count += 1
                else:
                    print(f'Fehler beim Herunterladen des Bildes von {img_url}.')
            except requests.exceptions.RequestException as e:
                print(f"Fehler bei Request für {img_url}: {e}")

    # WebDriver schließen
    driver.quit()

# Verwenden von Pool, um mehrere Seiten gleichzeitig zu verarbeiten
if __name__ == '__main__':
    with Pool(10) as p:
        p.map(download_images, urls)

print('Download abgeschlossen.')