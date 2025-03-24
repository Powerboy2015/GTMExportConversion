import os
# Final function
def compare_sheets(folder_path:str) -> dict[str,str]:
    tag = {}
    for file in os.listdir(folder_path):
        lines = get_lines(folder_path+"/"+file)
        compare_lines(tag,lines,file)
    return tag


# returns all the lines from the folder.
def get_lines(output_file: str) -> list[str]:
    with open(output_file,'r',encoding='utf-8') as file:
        return file.readlines()


# Compare lines and adds them to the holder. 
# If they are already in the holder, adds the filename to it.
def compare_lines(holder: dict,lines: list, file_name:str):
    addition = file_name.split("_")[1].strip('.json')
    for line in lines:
        if line not in holder.keys():
            holder[line] = [addition]
        elif line in holder.keys():
            holder[line].append(addition)        


def output_comparison(comparison_dict: dict[str,list[str]],output_file:str):
    
    with open(output_file,'w',encoding='utf-8') as file:
        
        for key,values in comparison_dict.items():
            # sets the empty text string that we fill
            text = "\t".join(values)
            #  loops through the list of copies and adds the addition 
            file.write(f"{key.strip('\n')}\t{text}\n")

