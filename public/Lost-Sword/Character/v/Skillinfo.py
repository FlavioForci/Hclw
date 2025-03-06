from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from deep_translator import GoogleTranslator

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

def translate_text(text):
    # Replace known Chinese names with their English equivalents first
    for cn_name in sorted(name_mapping.keys(), key=lambda x: -len(x)):
        text = text.replace(cn_name, name_mapping[cn_name])
    try:
        if not text.strip():
            return ""
        translator = GoogleTranslator(source='ko', target='en')
        return translator.translate(text)
    except Exception as e:
        print(f"Übersetzungsfehler: {str(e)}")
        return text

def extract_and_translate_content(url):
    driver = webdriver.Chrome()
    driver.get(url)
    content_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div.fr-view.article-content"))
    )
    content = content_element.text.strip()
    translated_content = translate_text(content)
    with open("translated_content.txt", "w", encoding="utf-8") as f:
        f.write(translated_content)
    print("Inhalt extrahiert und übersetzt.")

url = "https://arca.live/b/lostsword/126991072"
extract_and_translate_content(url)
