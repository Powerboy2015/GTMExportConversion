import os
from utils.convert_sheet import OutputToFile as to_sheet_text
import utils.Sheetur as Sheetur
import tkinter as tk
from tkinter import ttk
import utils.tkPrefabs as tPre

# files = [f for f in os.listdir("./JSON_imports") if os.path.isfile(os.path.join("./JSON_imports", f))]
# for file in files:
#     to_sheet_text(file)


# Sheetur.Compare_sheets('./JSON_imports')

color_table = {
    "blue":         "#182d4d",
    "green":        "#009b67",
    "light_green":  "#d2f0e3",
    "off_white" :   "#fff9f7",
    "red":          "#ff8484"
}

# Set default background for all ttk widgets using Style



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
files_head_div = tk.Frame(files_div,width=162,height=51,background=color_table["red"])
files_head_div.grid(column=0,row=0,padx=10,pady=10)
files_head_div.grid_propagate(False)

choose_files_text = tk.Label(files_head_div,text="Choose files", width=90,height=10,background=color_table["light_green"])
choose_files_text.grid(column=0,row=0)
# files head div

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