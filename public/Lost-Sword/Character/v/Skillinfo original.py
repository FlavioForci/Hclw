from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from deep_translator import GoogleTranslator
import multiprocessing
import time

# Manual mapping of Chinese names to English names
name_mapping = {
    "莉莎": "Lisa",
    "加拉哈德": "Galahad",
    "伊丽莎白": "Elizabeth",
    "维维安": "Vivian",
    "特里斯坦": "Tristan",
    "莉亚": "Ria",
    "兰恩": "Ran",
    "帕西瓦尔": "Percival",
    "摩尔加兹": "Morgause",
    "莫甘娜": "Morgana",
    "米娅": "Mia",
    "梅林": "Merlin",
    "露西": "Lucy",
    "色亚": "Lua",
    "莉莉丝": "Lilith",
    "瑟茜": "Circe",
    "凯伊": "Kay",
    "卡特琳": "Catherine",
    "圣女贞德": "Joan of Arc",
    "伊索尔德": "Isolde",
    "伊莎贝尔": "Isabelle",
    "桂妮维亚": "Guinevere",
    "加文": "Gawain",
    "恩雅": "Enya",
    "克里斯蒂娜": "Christina",
    "克莱尔": "Claire",
    "艾丹": "Aidan",
    "贝迪维尔": "Bedivere",
    "乌利恩": "Urien",
    "萨拉": "Sarah",
    "雷伊": "Rey",
    "妮妙": "Nymue",
    "梅里": "Maryy",
    "罗安娜": "Rowena",
    "加赫里斯": "Gaheris",
    "艾斯梅拉达": "Esmeralda",
    "贝林": "Baylin",
    "艾莲": "Elaine",
    "丽塔": "Rita",
    "瑞秋": "Rachel",
    "杰西": "Jessie",
    "艾琳": "Elin",
    "伊希斯": "Isis"
}

def close_popups(driver):
    """Schließt eventuelle Popups"""
    try:
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".popup-close, .close-button"))
        ).click()
        print("Popup geschlossen")
    except:
        pass

def create_output_dir(dir_name):
    """Erstellt Output-Verzeichnis wenn nicht vorhanden"""
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)

def translate_text(text):
    """Übersetzt Text mit deep-translator von Chinesisch zu Englisch, mit manuellen Übersetzungen für bestimmte Namen."""
    # Replace known Chinese names with their English equivalents first
    for cn_name in sorted(name_mapping.keys(), key=lambda x: -len(x)):
        text = text.replace(cn_name, name_mapping[cn_name])
    try:
        if not text.strip():
            return ""
        translator = GoogleTranslator(source='zh-CN', target='en')
        return translator.translate(text)
    except Exception as e:
        print(f"Übersetzungsfehler: {str(e)}")
        return text

def get_character_name(driver):
    """Extrahiert den Namen des Charakters aus dem <h1> Tag und übersetzt ihn"""
    try:
        name_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'h1.title'))
        )
        character_name = name_element.text.strip()
        translated_name = translate_text(character_name)
        return translated_name
    except Exception as e:
        print(f"Fehler beim Extrahieren des Charakternamens: {e}")
        return "Unknown"

def process_skill_tab_and_skills(driver, tab_index, character_name):
    """Verarbeitet einen Skill-Tab und speichert alle Skills in einzelnen Dateien."""
    try:
        tab = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, f".tab-item:nth-child({tab_index})"))
        )
        driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", tab)
        driver.execute_script("arguments[0].click();", tab)
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.tab-container"))
        )
        elements = driver.find_elements(By.CSS_SELECTOR, "div.tab-container")
        for index, element in enumerate(elements, 1):
            content = element.text.strip()
            translated = translate_text(content)
            translated_list = translated.split('\n')
            ignore_words = ["Rarity", "property", "Profession", "formation", "Race", "age", "Birthday", "height", "size", "Hobby", "weight", "gender"]
            filtered_content = []
            i = 0
            while i < len(translated_list):
                if translated_list[i] in ignore_words:
                    i += 2
                else:
                    filtered_content.append(translated_list[i])
                    i += 1
            filtered_translated = '\n'.join(filtered_content)
            folder_name = character_name + "_Skills"
            filename = f"{folder_name}/Skill{index}_Tab{tab_index}.txt"
            create_output_dir(folder_name)
            with open(filename, "w", encoding="utf-8") as f:
                f.write(f"Skill {index} (Tab {tab_index}) Information:\n")
                f.write("="*50 + "\n")
                f.write(filtered_translated)
            print(f"Skill {index} (Tab {tab_index}) gespeichert in {folder_name}")
        return f"Alle Skills für Tab {tab_index} verarbeitet."
    except Exception as e:
        return f"Fehler bei Tab {tab_index}: {str(e)}"

def process_card_info(driver, character_name):
    """Verarbeitet die Card Info."""
    try:
        card_info_elements = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.module-box"))
        )
        folder_name = character_name + "_Skills"
        create_output_dir(folder_name)
        for index, element in enumerate(card_info_elements):
            if index == 2:  # Nur CardInfo_3 speichern
                content = element.text.strip()
                translated = translate_text(content)
                filename = f"{folder_name}/CardInfo.txt"
                with open(filename, "w", encoding="utf-8") as f:
                    f.write(f"Card Info:\n")
                    f.write("="*50 + "\n")
                    f.write(translated)
                print(f"Card Info gespeichert in {folder_name}")
        return f"Card Info verarbeitet."
    except Exception as e:
        return f"Fehler bei Card Info: {str(e)}"

def cleanup_files(character_name):
    """Löscht und benennt Dateien nach der Verarbeitung."""
    folder_name = character_name + "_Skills"
    if os.path.exists(folder_name):
        for filename in os.listdir(folder_name):
            if filename.startswith("Skill2"):
                file_path = os.path.join(folder_name, filename)
                try:
                    os.remove(file_path)
                    print(f"Datei {filename} gelöscht.")
                except Exception as e:
                    print(f"Fehler beim Löschen von {filename}: {e}")
        skill3_files = sorted([f for f in os.listdir(folder_name) if f.startswith("Skill3")])
        if len(skill3_files) > 1:
            for filename in skill3_files[:-1]:
                file_path = os.path.join(folder_name, filename)
                try:
                    os.remove(file_path)
                    print(f"Datei {filename} gelöscht.")
                except Exception as e:
                    print(f"Fehler beim Löschen von {filename}: {e}")
        skill3_files = [f for f in os.listdir(folder_name) if f.startswith("Skill3")]
        if len(skill3_files) == 1:
            old_file_path = os.path.join(folder_name, skill3_files[0])
            new_file_path = os.path.join(folder_name, "CardInfo.txt")
            try:
                os.rename(old_file_path, new_file_path)
                print(f"Datei {skill3_files[0]} umbenannt in CardInfo.txt")
            except Exception as e:
                print(f"Fehler beim Umbenennen der Datei: {e}")
        skill1_files = sorted([f for f in os.listdir(folder_name) if f.startswith("Skill1_Tab")])
        for i, filename in enumerate(skill1_files):
            old_file_path = os.path.join(folder_name,filename)
            new_file_path = os.path.join(folder_name,f"Skill{i+1}.txt")
            try:
                os.rename(old_file_path,new_file_path)
                print(f"Datei {filename} wurde umbenannt in Skill{i+1}.txt")
            except Exception as e:
                print(f"Fehler beim Umbenennen von {filename}: {e}")

def process_url(url):
    """Verarbeitet eine einzelne URL."""
    driver = webdriver.Chrome()  # WebDriver für jeden Prozess
    try:
        driver.get(url)
        close_popups(driver)
        character_name = get_character_name(driver)
        for tab_index in range(1, 5):
            process_skill_tab_and_skills(driver, tab_index, character_name)
        process_card_info(driver, character_name)  # Aufrufen der neuen Funktion
        cleanup_files(character_name)  # Aufräumen der Dateien
        print(f"URL {url} verarbeitet.")
    except Exception as e:
        print(f"Fehler bei URL {url}: {e}")
    finally:
        driver.quit()

# **Beispielverwendung mit Multiprocessing**

urls = [
    "https://www.gamekee.com/lostsword/645310.html",
    "https://www.gamekee.com/lostsword/645311.html",
    "https://www.gamekee.com/lostsword/645312.html",
    "https://www.gamekee.com/lostsword/645313.html",
    "https://www.gamekee.com/lostsword/645314.html",
    "https://www.gamekee.com/lostsword/645315.html",
    "https://www.gamekee.com/lostsword/645316.html",
    "https://www.gamekee.com/lostsword/645318.html",
    "https://www.gamekee.com/lostsword/645319.html",
    "https://www.gamekee.com/lostsword/645320.html",
    "https://www.gamekee.com/lostsword/645321.html",
    "https://www.gamekee.com/lostsword/645322.html",
    "https://www.gamekee.com/lostsword/645323.html",
    "https://www.gamekee.com/lostsword/645324.html",
    "https://www.gamekee.com/lostsword/645325.html",
    "https://www.gamekee.com/lostsword/645326.html",
    "https://www.gamekee.com/lostsword/645327.html",
    "https://www.gamekee.com/lostsword/645328.html",
    "https://www.gamekee.com/lostsword/645329.html",
    "https://www.gamekee.com/lostsword/645330.html",
    "https://www.gamekee.com/lostsword/645331.html",
    "https://www.gamekee.com/lostsword/645332.html",
    "https://www.gamekee.com/lostsword/645333.html",
    "https://www.gamekee.com/lostsword/645334.html",
    "https://www.gamekee.com/lostsword/645389.html",
    "https://www.gamekee.com/lostsword/645494.html",
    "https://www.gamekee.com/lostsword/645513.html",
    "https://www.gamekee.com/lostsword/645894.html",
    "https://www.gamekee.com/lostsword/645897.html",
    "https://www.gamekee.com/lostsword/645900.html",
    "https://www.gamekee.com/lostsword/645902.html",
    "https://www.gamekee.com/lostsword/645903.html",
    "https://www.gamekee.com/lostsword/645904.html",
    "https://www.gamekee.com/lostsword/645911.html",
    "https://www.gamekee.com/lostsword/645917.html",
    "https://www.gamekee.com/lostsword/645921.html",
    "https://www.gamekee.com/lostsword/645923.html",
    "https://www.gamekee.com/lostsword/645926.html",
    "https://www.gamekee.com/lostsword/645945.html",
    "https://www.gamekee.com/lostsword/645947.html",
    "https://www.gamekee.com/lostsword/645948.html",
    "https://www.gamekee.com/lostsword/646826.html",
    "https://www.gamekee.com/lostsword/646883.html"
]

if __name__ == "__main__":
    start_time = time.time()
    with multiprocessing.Pool(processes=10) as pool:  # Anzahl der Prozesse anpassen
        pool.map(process_url, urls)
    print(f"Verarbeitung abgeschlossen in {time.time() - start_time:.2f} Sekunden.")
