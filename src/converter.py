import os
from PIL import Image
import pillow_heif


# Functionality class for converting HEIC files
class HEICConverter:
    @staticmethod
    def convert_heic_to_png_and_replace(input_path: str):
        """Converts HEIC file to PNG and replaces it"""
        try:
            heif_image = pillow_heif.open_heif(input_path)
            image = Image.frombytes(heif_image.mode, heif_image.size, heif_image.data)

            # Save the file as PNG in the same location
            output_path = os.path.splitext(input_path)[0] + ".png"
            image.save(output_path, "PNG")

            # Remove the original file
            os.remove(input_path)
            print(f"✔ Converted & Replaced: {input_path} → {output_path}")
        except Exception as e:
            print(f"Error converting {input_path}: {e}")

    @staticmethod
    def convert_all_heic_in_folder(folder_path: str):
        """Converts all HEIC files in the folder to PNG and deletes the old files"""
        try:
            for filename in os.listdir(folder_path):
                if filename.lower().endswith(".heic"):
                    input_file = os.path.join(folder_path, filename)
                    HEICConverter.convert_heic_to_png_and_replace(input_file)
        except Exception as e:
            print(f"Error converting files in {folder_path}: {e}")
