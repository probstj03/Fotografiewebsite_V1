import os
from PIL import Image, ExifTags

input_dir = "E:/Bilder/Website/"
output_dir = "C:/Users/probs/Meine Ablage/Dokumente/Programmieren/Websites/Fotografiewebsite_V1/"
number_offset = 0

def compress_images(folder_name):
    # Dateien einlesen und nach Aufnahmedatum sortieren
    files = list(os.scandir(input_dir + folder_name))
    
    # Sortierung nach Aufnahmedatum
    def get_capture_date(file):
        try:
            with Image.open(file.path) as img:
                exif_data = img._getexif()
                if exif_data:
                    exif_keys = {ExifTags.TAGS[key]: key for key in ExifTags.TAGS if key in exif_data}
                    if "DateTimeOriginal" in exif_keys:
                        return exif_data[exif_keys["DateTimeOriginal"]]
                    elif "DateTime" in exif_keys:
                        return exif_data[exif_keys["DateTime"]]
        except Exception as e:
            print(f"Warnung: {file.path} konnte nicht verarbeitet werden ({e}).")
        return "1111:11:11 11:11:11"  # Dummy-Datum für nicht analysierbare Dateien
    
    # Dateien nach Datum sortieren (neueste zuerst)
    files = sorted(files, key=get_capture_date, reverse=True)
    
    max_index = len(files) 
    index = max_index

    for file in files:
        input_path = file.path
        output_large = os.path.join("img/", folder_name, f"{folder_name.split('.')[0]}_{index + number_offset}.jpg")
        output_small = os.path.join("img/", folder_name, f"{folder_name.split('.')[0]}_small_{index + number_offset}.jpg")
        
        # Lade das Bild und seine EXIF-Daten
        with Image.open(input_path) as img:
            exif_data = img._getexif()
            metadata = extract_metadata(exif_data)

            # Komprimierung für große Bilder
            img_large = img.copy()
            img_large.thumbnail((2000, 2000))
            img_large.save(output_dir + output_large, quality=70)

            # Komprimierung für kleine Bilder
            img_small = img.copy()
            img_small.thumbnail((1000, 1000))
            img_small.save(output_dir + output_small, quality=40)
        
        # HTML-Code mit Metadaten erstellen
        metadata_str = "  |  ".join([f"{key}: {value}" for key, value in metadata.items()])
        print(f'<a href="{output_large}" data-lightbox="mygallery" '
              f'data-title="{metadata_str}">'
              f'<img loading="lazy" src="{output_small}">'
              f'</a>')

        index -= 1

def extract_metadata(exif_data):
    metadata = {}
    if exif_data:
        # Schlüssel und Namen zuordnen
        exif_keys = {ExifTags.TAGS[key]: key for key in ExifTags.TAGS if key in exif_data}
        # Nützliche Daten extrahieren
        if "Model" in exif_keys:
            camera_model = exif_data[exif_keys["Model"]]
            # Anpassung für Nikon Z 6_2
            if camera_model == "NIKON Z 6_2":
                metadata["Kamera"] = "NIKON Z6II"
            else:
                metadata["Kamera"] = camera_model
        if "LensModel" in exif_keys:
            metadata["Objektiv"] = exif_data[exif_keys["LensModel"]]
        if "FocalLength" in exif_keys:
            focal_length = exif_data[exif_keys["FocalLength"]]
            metadata["Brennweite"] = f"{float(focal_length):.1f}mm"
        if "ExposureTime" in exif_keys:
            exposure_time = exif_data[exif_keys["ExposureTime"]]
            exposure_value = float(exposure_time)
            if exposure_value < 1:
                # Belichtungszeit als Bruch darstellen
                numerator = exposure_time.numerator
                denominator = exposure_time.denominator
                metadata["Belichtung"] = f"1/{denominator}s"
            else:
                # Belichtungszeit als Dezimalzahl darstellen
                metadata["Belichtung"] = f"{exposure_value:.1f}s"
        if "ISOSpeedRatings" in exif_keys:
            metadata["ISO"] = exif_data[exif_keys["ISOSpeedRatings"]]
        if "FNumber" in exif_keys:
            f_number = exif_data[exif_keys["FNumber"]]
            metadata["Blende"] = f"f/{float(f_number):.1f}"
        
    return metadata

# Beispielaufruf
compress_images("kindergarten")
