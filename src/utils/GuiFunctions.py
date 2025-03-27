import tkinter as tk
from tkinter import filedialog
from src.gui import GLOBAL_CHOSEN_FILES



def get_files(inner_element: tk.Frame) -> list[str]:
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
        file_element.grid(column=1,row=filepaths.index(filepath),sticky=tk.W)
    GLOBAL_CHOSEN_FILES.append(filepaths)
    print(GLOBAL_CHOSEN_FILES)