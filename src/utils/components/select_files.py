import tkinter as tk
from src.utils import GuiFunctions as GFunc
from src.utils.colors import color_table



def select_files(content_div):
    # files div
    files_div = tk.Frame(content_div, width=181, height=438, background=color_table["light_green"])
    files_div.grid(column=0, row=0, padx=(0, 78),rowspan=2)
    files_div.grid_propagate(False)

    # files head div
    files_head_div = tk.Frame(files_div, width=162, height=51, background=color_table["light_green"])
    files_head_div.grid(column=0, row=0, padx=10, pady=(10, 0))

    # columns config
    files_head_div.grid_columnconfigure(0, weight=1)
    files_head_div.grid_columnconfigure(1, weight=1)
    files_head_div.grid_rowconfigure(1, weight=1)
    files_head_div.grid_propagate(False)
    #

    choose_files_text = tk.Label(files_head_div, text="Choose files", background=color_table["light_green"])
    choose_files_text.grid(column=0, row=0, sticky=tk.W)

    choose_files_button = tk.Button(files_head_div,
                                    text="Choose",
                                    background=color_table["blue"],
                                    foreground=color_table["light_green"],
                                    activebackground=color_table["blue"],
                                    activeforeground=color_table["light_green"],
                                    command=lambda: GFunc.get_files(scrollable_frame))
    choose_files_button.grid(column=1, row=0, sticky=tk.E)

    filename_list_text = tk.Label(files_head_div, text="Filenames", background=color_table["light_green"])
    filename_list_text.grid(column=0, row=1, columnspan=2, sticky="nsew")

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