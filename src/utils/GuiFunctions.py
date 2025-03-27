import tkinter as tk
from tkinter import filedialog




def get_files(inner_element: tk.Canvas) -> None:
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
