import os
from lib.convert_sheet import OutputToFile as to_sheet_text
import lib.Sheetur as Sheetur

files = [f for f in os.listdir("./JSON_imports") if os.path.isfile(os.path.join("./JSON_imports", f))]
for file in files:
    to_sheet_text(file)


Sheetur.Compare_sheets('./JSON_imports')