import os
import json

def read_skill_info(root_dir, character_name):
    skill_info = {}
    skills_dir = os.path.join(root_dir, f"{character_name}_Skills")
    
    if os.path.exists(skills_dir):
        for filename in os.listdir(skills_dir):
            if filename in ["Skill1.txt", "Skill2.txt", "Skill3.txt", "Skill4.txt"]:
                filepath = os.path.join(skills_dir, filename)
                try:
                    with open(filepath, "r", encoding="utf-8") as f:
                        lines = f.readlines()
                        skill_number = filename.split("Skill")[1].split(".txt")[0]
                        skill = {}
                        current_key = None
                        
                        # Skip first two lines
                        for line in lines[2:]:
                            line = line.strip()
                            if line:  # Skip empty lines
                                if ":" in line:
                                    key, value = line.split(":", 1)
                                    current_key = key.strip()
                                    skill[current_key] = value.strip()
                                else:
                                    if current_key:
                                        # Append to existing value
                                        skill[current_key] = skill[current_key] + " " + line
                                    else:
                                        # Use line as both key and value
                                        skill[line] = line
                                        current_key = line
                                        
                        skill_info[f"Skill {skill_number}"] = skill
                except Exception as e:
                    print(f"Fehler beim Lesen von {filename}: {e}")
    return skill_info

def read_card_info(root_dir, character_name):
    card_info = {}
    skills_dir = os.path.join(root_dir, f"{character_name}_Skills")
    
    if os.path.exists(skills_dir):
        card_file = os.path.join(skills_dir, "Cardinfo.txt")
        if os.path.exists(card_file):
            try:
                with open(card_file, "r", encoding="utf-8") as f:
                    lines = f.readlines()
                    card = {}
                    current_key = None
                    
                    # Skip first two lines
                    for line in lines[2:]:
                        line = line.strip()
                        if line:  # Skip empty lines
                            if ":" in line:
                                key, value = line.split(":", 1)
                                current_key = key.strip()
                                card[current_key] = value.strip()
                            else:
                                if current_key:
                                    # Append to existing value
                                    card[current_key] = card[current_key] + " " + line
                                else:
                                    # Use line as both key and value
                                    card[line] = line
                                    current_key = line
                                    
                    card_info["card"] = card
            except Exception as e:
                print(f"Fehler beim Lesen von Cardinfo.txt: {e}")
    return card_info

# Rest des Codes bleibt gleich...


def collect_character_data(root_dir):
    character_data = {}
    for folder_name in os.listdir(root_dir):
        character_dir = os.path.join(root_dir, folder_name)
        if os.path.isdir(character_dir) and folder_name.endswith("_Skills"):
            character_name = folder_name.replace("_Skills", "")
            skill_info = read_skill_info(root_dir, character_name)
            card_info = read_card_info(root_dir, character_name)
            character_data[character_name] = {**skill_info, **card_info}
    return character_data

# Pfad anpassen
root_dir = "./"
character_data = collect_character_data(root_dir)

with open("character_data.json", "w", encoding="utf-8") as f:
    json.dump(character_data, f, indent=4, ensure_ascii=False)

print("Daten erfolgreich verarbeitet!")
