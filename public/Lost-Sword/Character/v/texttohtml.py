import re
import os

def parse_skill_info(text):
    # Extrahiert den Namen und das Level der Fähigkeit (z.B. "Flash - Ultimate")
    name_level_pattern = r"([a-zA-Z\s\-]+)\s*\-\s*(Ultimate|Passive|passive)"
    match = re.search(name_level_pattern, text)
    skill_name = match.group(1).strip() if match else "Unknown Skill"
    skill_level = match.group(2).strip() if match else "Unknown Level"
    
    # Extrahiert die Damage-Info (z.B. "711/765/819/900/990% of Attack")
    damage_pattern = r"Causes\s([0-9\/]+)%\s*damage"
    damage_match = re.search(damage_pattern, text)
    damage_info = damage_match.group(1) if damage_match else "Unknown Damage"
    
    # Extrahiert den Effekt (z.B. "When the target unit is a lord, it causes 1 additional damage...")
    effect_pattern = r"Effect:\s*Additional\s*damage\s*When\s*the\s*target\s*unit\s*is\s*a\s*(.*?),\s*it\s*causes\s*(.*)"
    effect_match = re.search(effect_pattern, text)
    effect_info = effect_match.group(2) if effect_match else "No Effect"
    
    # Extrahiert den Target (z.B. "All Enemies")
    target_pattern = r"Target unit\s*(.*)"
    target_match = re.search(target_pattern, text)
    target_info = target_match.group(1) if target_match else "Unknown Target"
    
    # Extrahiert die Cooldown-Info (z.B. "32 seconds")
    cooldown_pattern = r"Cooling time\s*([\d]+)\s*second"
    cooldown_match = re.search(cooldown_pattern, text)
    cooldown_info = cooldown_match.group(1) if cooldown_match else "Unknown Cooldown"

    # Erstellen der HTML-Ausgabe
    html_output = f'''
    <div class="skill-description">
        <div class="skill-name">{skill_name}</div>
        <div class="skill-level">{skill_level}</div>
        <div class="skill-section">
            <div class="section-title">[Damage Dealt]</div>
            <div>Causes damage equal to [{damage_info}]% of Attack</div>
        </div>
        <div class="skill-section">
            <div class="section-title">[Effect: Additional Damage]</div>
            <div>{effect_info}</div>
        </div>
        <div class="skill-section">
            <div class="section-title">[Target]</div>
            <div>{target_info}</div>
        </div>
        <div class="skill-section">
            <div class="section-title">[Cooldown]</div>
            <div>{cooldown_info} Second(s)</div>
        </div>
    </div>
    '''
    return html_output

def convert_txt_to_html(input_folder, output_folder):
    # Geht alle .txt-Dateien im angegebenen Ordner durch
    for filename in os.listdir(input_folder):
        if filename.endswith(".txt"):
            input_file_path = os.path.join(input_folder, filename)
            output_file_path = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}.html")
            
            with open(input_file_path, 'r') as file:
                text = file.read()
            
            html_content = parse_skill_info(text)
            
            with open(output_file_path, 'w') as file:
                file.write(html_content)
            
            print(f"HTML output saved to {output_file_path}")

# Beispielaufruf
input_folder = './Mia_Skills'  # Der Ordner mit den Textdateien
output_folder = './output_html'  # Der Ordner, in dem die HTML-Dateien gespeichert werden

# Sicherstellen, dass der Ausgabeordner existiert
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

convert_txt_to_html(input_folder, output_folder)
