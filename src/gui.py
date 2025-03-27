import os
from utils.convert_sheet import OutputToFile as to_sheet_text
import utils.Sheetur as Sheetur
import tkinter as tk
from tkinter import ttk
import utils.tkPrefabs as tPre
import utils.GuiFunctions as GFunc

# files = [f for f in os.listdir("./JSON_imports") if os.path.isfile(os.path.join("./JSON_imports", f))]
# for file in files:
#     to_sheet_text(file)

# Sheetur.Compare_sheets('./JSON_imports')



GLOBAL_CHOSEN_FILES = []

color_table = {
    "blue":         "#182d4d",
    "green":        "#009b67",
    "light_green":  "#d2f0e3",
    "off_white" :   "#fff9f7",
    "red":          "#ff8484"
}
def insert_files(destination):
    GLOBAL_CHOSEN_FILES = GFunc.get_files(destination)


root = tk.Tk()
root.title("SheeturGTM")
root.geometry("900x600")
root.resizable(False,False)
# root.config(background=color_table['off_white'])
root.grid_propagate(False)


#Title div
title_div = tk.Frame(root,width=900,height=104,background=color_table["green"])
title_div.grid(column=0,row=0,sticky="ew")
title_div.grid_propagate(False)
title_div.columnconfigure(0, weight=1)  # we sorta encapsulate by using all columns

title = tPre.create_label(title_div,"SheeturGTM", 14)
title.grid(column=0,row=0,pady=10,sticky="ew")
title.config(background=color_table["green"])

under_text = tk.Label(title_div,text="Relevant onlines easy container comparer and extractor")
under_text.grid(column=0,row=1,pady=10,sticky="ew")
under_text.config(background=color_table["green"])
#Title div

# Content div
content_div = tk.Frame(root,width=744,height=430,background=color_table["off_white"])
content_div.grid(column=0,row=1,pady=33,padx=78)
content_div.grid_propagate(False)

# files div
files_div = tk.Frame(content_div,width=181,height=438,background=color_table["light_green"])
files_div.grid(column=0,row=0,padx=(0,78))
files_div.grid_propagate(False)

# files head div
files_head_div = tk.Frame(files_div,width=162,height=51,background=color_table["light_green"])
files_head_div.grid(column=0,row=0,padx=10,pady=(10,0))

# columns config
files_head_div.grid_columnconfigure(0, weight=1)
files_head_div.grid_columnconfigure(1, weight=1)
files_head_div.grid_rowconfigure(1, weight=1)
files_head_div.grid_propagate(False)
#

choose_files_text = tk.Label(files_head_div,text="Choose files",background=color_table["light_green"])
choose_files_text.grid(column=0,row=0,sticky=tk.W)

choose_files_button = tk.Button(files_head_div,
                                text="Choose",
                                background=color_table["blue"],
                                foreground=color_table["light_green"],
                                activebackground=color_table["blue"],
                                activeforeground=color_table["light_green"],
                                command= lambda: GFunc.get_files(scrollable_frame))
choose_files_button.grid(column=1,row=0,sticky=tk.E)

filename_list_text = tk.Label(files_head_div,text="Filenames",background=color_table["light_green"])
filename_list_text.grid(column=0,row=1,columnspan=2,sticky="nsew")
# files head div

# --- files body div  ---
files_body_div = tk.Frame(files_div, width=181, height=367, borderwidth=0, relief="flat",background=color_table["green"])
files_body_div.grid(column=0, row=1)
files_body_div.grid_propagate(False)
files_body_div.grid_rowconfigure(0, weight=1)
files_body_div.grid_columnconfigure(0, weight=1)

# --- Canvas ---
file_list_display = tk.Canvas(files_body_div, background=color_table['green'], borderwidth=0, relief="flat",highlightthickness=0)
file_list_display.grid(column=0, row=0, sticky="nsew",padx=(0,0),pady=(0,0))

# --- Horizontal Scrollbar ---
file_list_scroller = tk.Scrollbar(files_body_div, orient=tk.HORIZONTAL, command=file_list_display.xview)
file_list_scroller.grid(column=0, row=1, sticky="ew")  # Only stretch horizontally!

file_list_display.configure(xscrollcommand=file_list_scroller.set)

# --- Scrollable Frame inside Canvas ---
scrollable_frame = tk.Frame(file_list_display,borderwidth=0, relief="flat",background=color_table["green"])
canvas_window = file_list_display.create_window((0, 0), window=scrollable_frame, anchor="nw")

def on_frame_configure(event):
    file_list_display.configure(scrollregion=file_list_display.bbox("all"))

scrollable_frame.bind("<Configure>", on_frame_configure)
# --- files body div ---

# files div

to_sheets_div = tk.Frame(content_div,width=486,height=180,background=color_table["light_green"])
to_sheets_div.grid(column=1,row=0,sticky="n",pady=(0,70))
to_sheets_div.grid_propagate(False)

export_div = tk.Frame(content_div,width=486,height=180,background=color_table["light_green"])
export_div.grid(column=1,row=0,sticky="s")
export_div.grid_propagate(False)

print(export_div.grid_info())
# Content div




root.update_idletasks()  # Forces Tkinter to calculate sizes

# Get the actual usable space (client area)
usable_width = root.winfo_width() - (root.winfo_rootx() - root.winfo_x()) * 2
usable_height = root.winfo_height() - (root.winfo_rooty() - root.winfo_y())

print("Window size (including title bar):", root.winfo_width(), "x", root.winfo_height())
print("Usable space (excluding title bar):", usable_width, "x", usable_height)

    
root.mainloop()