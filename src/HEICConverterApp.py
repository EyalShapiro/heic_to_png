import os
import sys
from tkinter import Tk, filedialog, Button, Label
from converter import HEICConverter  # Corrected import statement

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), ".")))


class HEICConverterApp:
    def __init__(self, root, converter: HEICConverter):
        self.root = root
        self.converter = converter  # Creating an instance of the HEICConverter class
        self.root.title("HEIC to PNG Converter")
        self.root.geometry("400x250")

        self.selected_folder = None  # Variable to store the selected folder

        # Create UI components
        self.label = Label(
            root, text="Select a folder to convert HEIC files", padx=20, pady=20
        )
        self.label.pack()

        self.select_folder_button = Button(
            root, text="Select Folder", command=self.select_folder
        )
        self.select_folder_button.pack()

        self.confirm_button = Button(
            root,
            text="Confirm and Convert Files",
            state="disabled",
            command=self.convert_all_files_in_folder,
        )
        self.confirm_button.pack()

        self.status_label = Label(
            root, text="", padx=20, pady=20
        )  # Status label for completion message
        self.status_label.pack()

    def select_folder(self):
        """Select a folder"""
        self.selected_folder = filedialog.askdirectory()
        if self.selected_folder:
            self.label.config(text=f"Folder selected: \n{self.selected_folder}")
            self.confirm_button.config(state="normal")  # Enable the confirm button

    def convert_all_files_in_folder(self):
        """Convert all files in the folder to PNG"""
        if self.selected_folder:
            self.converter.convert_all_heic_in_folder(self.selected_folder)
            self.label.config(
                text=f"Conversion completed for folder: {self.selected_folder}"
            )
            self.status_label.config(
                text="All files have been converted!"
            )  # Show completion message
            self.confirm_button.config(
                state="disabled"
            )  # Disable the confirm button after conversion


def runGui():  # GUI class managing the interface

    root = Tk()
    converter = HEICConverter()  # Create an instance of the HEICConverter class
    app = HEICConverterApp(
        root, converter
    )  # Pass the converter instance to the GUI class
    root.mainloop()
    return app


if __name__ == "__main__":
    runGui()
