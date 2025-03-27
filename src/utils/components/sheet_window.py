import tkinter as tk
from src.utils.colors import color_table
from src.gui import GLOBAL_SHEET_DESTINATION
from src.utils.GuiFunctions import get_file_destination as get_destination


def set_destination_variable(destination_label: tk.Label) -> None:
    global GLOBAL_SHEET_DESTINATION
    destination = get_destination(destination_label)
    GLOBAL_SHEET_DESTINATION = destination

def sheet_window(content_div):
    outer_div = tk.Frame(content_div, width=486, height=180, background=color_table["light_green"])
    outer_div.grid(column=1, row=1,sticky=tk.NSEW,pady=(35,0))
    outer_div.grid_propagate(False)

    inner_div = tk.Frame(outer_div, width=466, height=160, bg=color_table["light_green"])
    inner_div.grid(padx=10,pady=10)
    inner_div.grid_propagate(False)

    title_label = tk.Label(inner_div, text="Compare Files",bg=color_table["light_green"])
    title_label.grid(column=0, row=0, sticky=tk.NW)

    choose_destination_container = tk.Frame(inner_div,bg=color_table["green"],width=350,height=20)
    choose_destination_container.grid(column=0, row=1,sticky=tk.NSEW)
    choose_destination_container.grid_propagate(False)
    choose_destination_container.grid_rowconfigure(0, weight=1)

    choose_destination_label = tk.Label(choose_destination_container,bg=color_table["green"],text="Choose destination")
    choose_destination_label.grid(column=0,row=0,sticky="")

    choose_destination_button = tk.Button(inner_div,
                                          bg=color_table["blue"],
                                          fg=color_table['light_green'],
                                          activebackground=color_table["blue"],
                                          activeforeground=color_table["light_green"],
                                          text="Choose destination",
                                          command=lambda: set_destination_variable(choose_destination_label))
    choose_destination_button.grid(column=1,row=1,sticky=tk.NSEW)

    export_button = tk.Button(inner_div,text="Compare containers", bg=color_table["blue"],fg=color_table['light_green'],activebackground=color_table["blue"],activeforeground=color_table["light_green"])
    export_button.grid(column=0,row=2,sticky=tk.SW,pady=(89,0))




