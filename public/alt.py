import os
import re

# Funktion zur Konvertierung des Dateinamens in eine lesbare Beschreibung
def convert_filename_to_alt(filename):
    # Entferne den Dateipfad und die Erweiterung (.jpg, .png, .mp4 etc.)
    name_without_extension = filename.split('/')[-1].split('.')[0]
    # Ersetze Bindestriche und Unterstriche durch Leerzeichen und formatiere die Wörter
    return name_without_extension.replace('-', ' ').replace('_', ' ').capitalize()

# Funktion zum Bearbeiten der HTML-Dateien
def process_html_files(folder_path):
    changes = []
    # Durchlaufe alle Dateien und Unterordner
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".html"):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                # Suche nach img-Tags ohne alt-Attribut und füge es hinzu
                new_content, img_changes = re.subn(
                    r'(<img\s+[^>]*src="([^"]+)")((?!\s+alt=)[^>])*>',
                    lambda m: f'{m.group(1)} alt="{convert_filename_to_alt(m.group(2))}">',
                    content
                )

                # Suche nach video-Tags ohne aria-label-Attribut und füge es hinzu
                new_content, video_changes = re.subn(
                    r'(<video\s+[^>]*src="([^"]+)")((?!\s+aria-label=)[^>])*>',
                    lambda m: f'{m.group(1)} aria-label="{convert_filename_to_alt(m.group(2))}">',
                    new_content
                )

                # Wenn Änderungen vorgenommen wurden, speichere die Datei neu
                if img_changes > 0 or video_changes > 0:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    changes.append({
                        "file": file_path,
                        "img_changes": img_changes,
                        "video_changes": video_changes
                    })

    return changes

# Funktion zur Ausgabe der Änderungen
def print_changes(changes):
    for change in changes:
        print(f'Datei: {change["file"]}')
        if change["img_changes"] > 0:
            print(f'  {change["img_changes"]} Bild-Tag(s) geändert')
        if change["video_changes"] > 0:
            print(f'  {change["video_changes"]} Video-Tag(s) geändert')

if __name__ == "__main__":
    folder_path = input("Gib den Pfad zum Ordner mit den HTML-Dateien an: ")

    if os.path.exists(folder_path):
        changes = process_html_files(folder_path)
        if changes:
            print("Änderungen vorgenommen in den folgenden Dateien:")
            print_changes(changes)
        else:
            print("Keine Änderungen notwendig.")
    else:
        print("Der angegebene Pfad existiert nicht.")
