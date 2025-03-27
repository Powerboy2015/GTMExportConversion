import tkinter as tk
from tkinter import filedialog
from src.gui import GLOBAL_CHOSEN_FILES
from src.gui import GLOBAL_EXPORT_DESTINATION
from src.gui import GLOBAL_SHEET_DESTINATION
from src.utils.convert_sheet import convert_to_csv


def get_files(inner_element: tk.Frame) -> tuple[str]:
    """
    Opens a dialog and let's you select files. Then fills the given element with the folder paths.

    Parameters:
    file_list_display (tk.Canvas): the current canvas to display the filepaths into.

    """
    filepaths = filedialog.askopenfilenames(
        title="Select GTM container exports",
        filetypes=[("Json files", "*.json")]
    )
    for filepath in filepaths:
        file_element = tk.Label(inner_element, text=filepath, background="#009b67")
        file_element.grid(column=1, row=filepaths.index(filepath), sticky=tk.W)
    global GLOBAL_CHOSEN_FILES
    GLOBAL_CHOSEN_FILES = filepaths
    print(GLOBAL_CHOSEN_FILES)


def get_file_destination(destination_label: tk.Label) -> str:
    """
    Opens a dialog to choose a folder
    :param destination_label: tk.Label - the label where the folder path should be displayed.
    :return: str - the path to the selected folder.
    """
    folder_destination = filedialog.askdirectory(title="Select destination folder")
    destination_label.config(text=folder_destination)
    return folder_destination

def export_to_csv():
    convert_to_csv(GLOBAL_CHOSEN_FILES,GLOBAL_EXPORT_DESTINATION)