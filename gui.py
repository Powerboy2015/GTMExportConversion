import os
from convert_sheet import OutputToFile
import compare_sheets as sheetr
import Sheetur

# files = [f for f in os.listdir("./JSON_imports") if os.path.isfile(os.path.join("./JSON_imports", f))]
# for file in files:
#     OutputToFile(file)

# # Compares sheets and returns and
# #  dictionary with the names and the values.
# compared_sheet = sheetr.compare_sheets('./JSON_outputs')
# # outputs the dictionary into a 
# sheet = sheetr.output_comparison(compared_sheet,'compared_sheets/output.txt')

Sheetur.Compare_sheets('./JSON_imports')