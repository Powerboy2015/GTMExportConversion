import tkinter as tk
import utils.tkPrefabs as tPre




GLOBAL_CHOSEN_FILES = ()
GLOBAL_EXPORT_DESTINATION = []
GLOBAL_SHEET_DESTINATION = []
GLOBAL_COLOR_TABLE = {
    "blue":         "#182d4d",
    "green":        "#009b67",
    "light_green":  "#d2f0e3",
    "off_white" :   "#fff9f7",
    "red":          "#ff8484"
}

from utils.colors import color_table
def main():

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
    content_div.grid_rowconfigure(0, weight=1)
    content_div.grid_rowconfigure(1, weight=1)  # for row 2
    content_div.grid_columnconfigure(0, weight=1)
    content_div.grid_columnconfigure(1, weight=1)

    # files head div

    from utils.components.select_files import select_files
    select_files(content_div)

    # the comparison window component
    from utils.components.sheet_window import sheet_window
    sheet_window(content_div)

    # the export window component
    from utils.components.export_window import export_window
    export_window(content_div)

    root.update_idletasks()  # Forces Tkinter to calculate sizes

    root.mainloop()

if __name__ == "__main__":
    main()