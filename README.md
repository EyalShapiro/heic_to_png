# HEIC to PNG Converter

This application is a simple GUI-based tool to convert HEIC files to PNG format. It allows users to select a folder, and the application will automatically convert all HEIC files in that folder to PNG, replacing the original HEIC files.

## Features

- Choose a folder using a simple dialog
- Convert all HEIC files in the folder to PNG format
- Original files are replaced with the PNG versions
- Status updates shown in the UI

## Requirements

- Python 3.x
- Pillow
- pillow-heif
- tkinter

## Installation

To run this application, you need to have Python 3.x installed. After that, install the dependencies with pip:

```bash
pip install -r requirements.txt
```

## Usage

Run the application using the following command:

```bash
python main.py
```

## Code Overview

### `HeicConverterPng` Class

This class provides static methods to convert HEIC files to PNG format.

- `convert_heic_to_png_and_replace(input_path: str) -> bool`

  - Converts a single HEIC file to PNG and replaces the original file.
  - **Parameters:**
    - `input_path` (str): The path to the HEIC file.
  - **Returns:**
    - `bool`: True if the conversion was successful, False otherwise.

- `convert_all_heic_in_folder(folder_path: str) -> list`
  - Converts all HEIC files in the specified folder to PNG format.
  - **Parameters:**
    - `folder_path` (str): The path to the folder containing HEIC files.
  - **Returns:**
    - `list`: A list of filenames that failed to convert.

### `ConverterUiApp` Class

This class provides a Tkinter-based GUI for the HEIC to PNG conversion tool.

- `__init__(self, root=None)`

  - Initializes the GUI application.
  - **Parameters:**
    - `root` (optional): The root window for the Tkinter application.

- `select_folder(self)`

  - Opens a dialog to select a folder containing HEIC files.

- `convert_all_files_in_folder(self)`

  - Converts all HEIC files in the selected folder to PNG format.

- `startGui(self)`
  - Runs the Tkinter main loop to start the GUI.

### `main` Function

This function initializes and starts the `ConverterUiApp`.

```python
def main():
    app = ConverterUiApp()
    app.startGui()
```

To run the application, execute the `main.py` script.
