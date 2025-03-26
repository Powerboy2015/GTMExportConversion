import tkinter as tk
from tkinter import filedialog


def create_label(parent: tk,text_string: str,font_size:int)->tk.Label:
    label = tk.Label(parent, text=text_string, font=("Arial",font_size))
    return label


def get_file_path(label: tk.Text):
    # Open a file dialog and get the file path
    file_path = filedialog.askopenfilenames(title="select files:")
    # deletes current text and opens input up for editing
    label.delete(1.0, tk.END)
    label.config(state=tk.NORMAL)

    # if a file was selected, goes through each file and adds it's name to the input.
    if file_path:
        for file in file_path:
            label.insert(tk.END, f"{file}\n")
    else:
        label.config(text="No file selected")
    
    # recloses label
    label.config(state=tk.DISABLED)
    

def create_read_entry(parent: tk,text_var: str,font_size:int,xwidth: int)->tk.Entry:
    entry = tk.Entry(parent,textvariable=text_var, state="readonly",font=("Arial",font_size),width=xwidth)
    return entry