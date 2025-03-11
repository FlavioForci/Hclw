import os
from PIL import Image

# Verzeichnis, in dem die PNG-Dateien gesucht werden sollen
input_directory = './charakter_bilder'  # Startverzeichnis (du kannst es anpassen)

# Funktion zur Konvertierung von Bildern in WebP
def convert_to_webp(input_path, output_path):
    try:
        with Image.open(input_path) as img:
            img.save(output_path, 'webp')
            print(f'Konvertiert: {input_path} -> {output_path}')
            
            # Löschen der Original PNG-Datei
            os.remove(input_path)
            print(f'Gelöscht: {input_path}')
            
    except Exception as e:
        print(f'Fehler beim Konvertieren von {input_path}: {e}')

# Funktion, um durch alle Unterordner zu gehen und PNG- und JPG-Dateien zu konvertieren
def convert_images_in_directory(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg')):
                input_path = os.path.join(root, file)
                output_file = os.path.splitext(file)[0] + '.webp'
                output_path = os.path.join(root, output_file)
                convert_to_webp(input_path, output_path)

# Starte die Konvertierung
convert_images_in_directory(input_directory)