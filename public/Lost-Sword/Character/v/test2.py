import os
import json
import re

def parse_skill_content(content):
    skill = {}
    lines = [line.strip() for line in content.split('\n') if line.strip()]
    
    if not lines:
        return skill
    
    # Extrahiere Typ und Name aus der ersten Zeile
    first_line = lines[0]
    if " - Ultimate" in first_line:
        skill["type"] = "Ultimate"
        skill["name"] = first_line.split(" - ")[0].strip()
    elif "-active" in first_line:
        skill["type"] = "Active"
        skill["name"] = first_line.split("-active")[0].strip()
    elif "-passive" in first_line:
        skill["type"] = "Passive"
        skill["name"] = first_line.split("-passive")[0].strip()
    
    # Verarbeite die restlichen Zeilen
    i = 1
    while i < len(lines):
        line = lines[i]
        
        # Handle Key-Value-Paare mit Doppelpunkt
        if ":" in line:
            key, value = line.split(":", 1)
            key = key.strip()
            value = value.strip()
            skill[key] = value
            i += 1
        else:
            # Handle Key-Value-Paare ohne Doppelpunkt (nächste Zeile ist der Wert)
            key = line
            if i + 1 < len(lines) and ":" not in lines[i + 1]:
                value = lines[i + 1]
                skill[key] = value
                i += 2
            else:
                skill[key] = ""
                i += 1
    
    return skill

def read_skill_info(root_dir, character_name):
    skill_info = {}
    skills_dir = os.path.join(root_dir, f"{character_name}_Skills")
    
    if os.path.exists(skills_dir):
        for filename in sorted(os.listdir(skills_dir)):
            if filename.startswith("Skill") and filename.endswith(".txt"):
                filepath = os.path.join(skills_dir, filename)
                try:
                    with open(filepath, "r", encoding="utf-8") as f:
                        content = f.read()
                        content = content.split('==================================================', 1)[-1]
                        skill_number = re.search(r'\d+', filename).group()
                        skill = parse_skill_content(content)
                        skill_info[f"Skill {skill_number}"] = skill
                except Exception as e:
                    print(f"Error reading {filename}: {e}")
    return skill_info

def read_card_info(root_dir, character_name):
    card_info = {}
    card_file = os.path.join(root_dir, f"{character_name}_Skills", "Cardinfo.txt")
    
    if os.path.exists(card_file):
        try:
            with open(card_file, "r", encoding="utf-8") as f:
                content = f.read()
                content = content.split('==================================================', 1)[-1]
                card = parse_skill_content(content)
                card_info["card"] = card
        except Exception as e:
            print(f"Error reading card info: {e}")
    return card_info

def collect_character_data(root_dir):
    character_data = {}
    for folder_name in os.listdir(root_dir):
        if folder_name.endswith("_Skills"):
            character_name = folder_name.replace("_Skills", "")
            character_data[character_name] = {
                **read_skill_info(root_dir, character_name),
                **read_card_info(root_dir, character_name)
            }
    return character_data

def main():
    root_dir = "./"
    character_data = collect_character_data(root_dir)
    
    with open("character_data.json", "w", encoding="utf-8") as f:
        json.dump(character_data, f, indent=4, ensure_ascii=False)
    
    print("Daten erfolgreich verarbeitet!")

if __name__ == "__main__":
    main()
