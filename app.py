import os
from PIL import Image
import pillow_heif


# todo:build gui and chnage the path to the folder and add a button to convert the files
def convert_heic_to_png_and_replace(input_path: str):
    """ממיר קובץ HEIC ל-PNG ומחליף אותו"""
    heif_image = pillow_heif.open_heif(input_path)
    image = Image.frombytes(heif_image.mode, heif_image.size, heif_image.data)

    # שמירת הקובץ כ-PNG באותו מיקום
    output_path = os.path.splitext(input_path)[0] + ".png"
    image.save(output_path, "PNG")

    # מחיקת הקובץ המקורי
    os.remove(input_path)
    print(f"✔ Converted & Replaced: {input_path} → {output_path}")


def convert_all_heic_in_folder(folder_path: str):
    """ממיר את כל קובצי ה-HEIC בתיקייה ל-PNG ומוחק את הקבצים הישנים"""
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(".heic"):
            input_file = os.path.join(folder_path, filename)
            convert_heic_to_png_and_replace(input_file)


# שימוש - שנה את הנתיב לתיקייה שלך
folder_path = "demo/"
convert_all_heic_in_folder(folder_path)
