import os
from PIL import Image
import numpy as np
import csv

#input_dir = "E:/Bilder/Website/"
input_dir = "/Volumes/JULIAN_M1/Bilder/Website/"
#output_dir = "C:/Users/probs/OneDrive/Dokumente/Programmieren/Websites/Fotografiewebsite_V1/"
output_dir = "/Users/julian/Library/CloudStorage/GoogleDrive-probstj03@gmail.com/Meine Ablage/Dokumente/Programmieren/Websites/Fotografiewebsite_V1/"

def compress_images(folder_name, data=True):

  

    files = sorted(os.scandir(input_dir + folder_name), key=lambda f: f.stat().st_ctime, reverse=True)
    max_index = len(files) 
    index = max_index
    if data:
        with open(output_dir + "img/" + folder_name + "/" + folder_name+ ".csv", newline='', encoding='utf-8') as csvfile:
            csv_reader = csv.reader(csvfile)
        
            data = []
        
            for row in csv_reader:
                data.append(row[0]) 
        


    for file in files:  # Durchlaufe die Dateien in aufsteigender Reihenfolge

                    input_path = file.path
                    output_large = os.path.join("img/",folder_name,  f"{folder_name.split('.')[0]}_{index}.jpg")
                    output_small = os.path.join("img/",folder_name, f"{folder_name.split('.')[0]}_small_{index}.jpg")
                    
                    with Image.open(input_path) as img:
                        # Komprimierung für große Bilder
                        img_large = img.copy()
                        img_large.thumbnail((2000, 2000))
                        img_large.save(output_dir + output_large, quality=70)

                        # Komprimierung für kleine Bilder
                        img_small = img.copy()
                        img_small.thumbnail((1000, 1000))
                        img_small.save(output_dir + output_small, quality=40)
                    
                    # HTML Code printen
                    if data:
                        print(f'<a href="{output_large}" data-lightbox="mygallery" '
                            f'data-title="{data[index-1]}"'
                            f'><img src="{output_small}">'
                            f'</a>')
                    else:
                        print(f'<a href="{output_large}" data-lightbox="mygallery" '
                            f'><img loading="lazy" src="{output_small}">'
                            f'</a>')
                    index -= 1 
                        # Verringere die Nummerierung für das nächste Bild


            
                

# Beispielaufruf
compress_images("shooting", False)
