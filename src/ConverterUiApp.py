import os
import sys
from tkinter import Tk, filedialog, Button, Label, PhotoImage

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), ".")))

from HeicConverterPng import HeicConverterPng


class ConverterUiApp(Tk):
    def __init__(self, root=None):
        super().__init__() if root is None else super().__init__(root)
        self.title("HEIC to PNG Converter")
        self.geometry("400x250")
        self.selected_folder = None
        # Update the icon path to use an absolute path
        icon_path = os.path.join(os.path.dirname(__file__), "assets", "icon.png")
        p1 = PhotoImage(file=icon_path)

        # Setting icon of master window
        self.iconphoto(False, p1)
        self._create_widgets(p1)

    def _create_widgets(self, p1):
        """Creates UI elements"""
        self.label = Label(
            self, text="Select a folder to convert HEIC files", padx=20, pady=20
        )
        self.icon_label = Label(self)
        self.icon_label.pack()
        self.label.pack()

        self.select_folder_button = Button(
            self, text="Select Folder", command=self.select_folder
        )
        self.select_folder_button.pack()

        self.confirm_button = Button(
            self,
            text="Confirm and Convert Files",
            state="disabled",
            command=self.convert_all_files_in_folder,
        )
        self.confirm_button.pack()

        self.status_label = Label(self, text="", padx=20, pady=20)
        self.status_label.pack()

    def select_folder(self):
        """Select a folder"""
        self.selected_folder = filedialog.askdirectory()
        if self.selected_folder:
            self.label.config(text=f"Folder selected: \n{self.selected_folder}")
            self.confirm_button.config(state="normal")

    def convert_all_files_in_folder(self):
        """Convert all HEIC files in the folder to PNG"""
        if self.selected_folder:
            failed_files = HeicConverterPng.convert_all_heic_in_folder(
                self.selected_folder
            )
            text_label = ""
            if failed_files is None:
                text_label = "Error occurred during conversion!"
            elif failed_files:
                text_label = f"Failed to convert: {', '.join(failed_files)}"
            else:
                text_label = "All files have been converted!"
            self.status_label.config(text=text_label)
            self.confirm_button.config(state="disabled")

    def startGui(self):
        """Runs the GUI"""
        self.mainloop()


def main():
    app = ConverterUiApp()
    app.startGui()


if __name__ == "__main__":
    main()
