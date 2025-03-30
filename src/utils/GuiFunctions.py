import tkinter as tk
from tkinter import filedialog
from src.utils.convert_sheet import convert_to_csv
from src.utils.sheet_comparison import  to_report

# these three globals get altered when the functions present here get called.
GLOBAL_CHOSEN_FILES = ()
GLOBAL_EXPORT_DESTINATION = ""
GLOBAL_SHEET_DESTINATION = ""

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

def get_export_destination(destination_label: tk.Label) -> str:
    """
    Opens a dialog to choose a folder
    :param destination_label: tk.Label - the label where the folder path should be displayed.
    :return: str - the path to the selected folder.
    """
    folder_destination = filedialog.askdirectory(title="Select destination folder")
    destination_label.config(text=folder_destination)
    global GLOBAL_EXPORT_DESTINATION
    GLOBAL_EXPORT_DESTINATION = folder_destination
    return folder_destination

def get_sheet_destination(destination_label: tk.Label) -> str:
    """
    Opens a dialog to choose a folder
    :param destination_label: tk.Label - the label where the folder path should be displayed.
    :return: str - the path to the selected folder.
    """
    folder_destination = filedialog.askdirectory(title="Select destination folder")
    destination_label.config(text=folder_destination)
    global GLOBAL_SHEET_DESTINATION
    GLOBAL_SHEET_DESTINATION = folder_destination
    return folder_destination

def export_to_csv():
    print(f'file location: {GLOBAL_EXPORT_DESTINATION}')
    convert_to_csv(GLOBAL_CHOSEN_FILES,GLOBAL_EXPORT_DESTINATION)

def compare_containers():
    print(GLOBAL_CHOSEN_FILES)
    print(f'file location: {GLOBAL_SHEET_DESTINATION}')
    to_report(GLOBAL_CHOSEN_FILES,GLOBAL_SHEET_DESTINATION)