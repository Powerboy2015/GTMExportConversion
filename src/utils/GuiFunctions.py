import tkinter as tk
from tkinter import filedialog




def get_files(list_display: tk.Canvas) -> None:
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
        list_display.insert(tk.END, filepath)
    """Updates the element size"""
    list_display.configure(scrollregion=list_display.bbox("all"))
