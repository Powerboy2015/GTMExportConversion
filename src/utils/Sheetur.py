from utils.jsonny import FileToJson
import os
from collections import defaultdict
# Sheetur is used to compare GTM containers.


# The idea is that we open all files and put them in a dict.
# We go through each .json file
# If we find a tag that we don't have yet, we add it, and a prefix.
# If we do have it, add the tag.
# If we don't have it in our main file, and we do have it in our dict, add a -.
def Compare_sheets(folder_path:str): 
    jsonFiles = {}
    
    # Loops through each file and 
    # returns each respective json file under their adverb
    for file in os.listdir(folder_path):
        name = file.split("_")[1]
        jsonFiles[name] = FileToJson(os.path.join(folder_path,file))
    
    # if the value is empty, set it by default as a dictionary when called upon.
    comparison = defaultdict(dict)
    
    # loop through each file. and gets a list of tags and triggers.
    for name, json in jsonFiles.items():
        tags = json['containerVersion']['tag']

        # Loops through all tags
        comparison = compare_tag_to_files(tags,jsonFiles,comparison)
    
    # Returns the output
    output_to_file('compared_sheets/output.txt',comparison)

def compare_tag_to_files(tags:list[str],files: dict, output_dict:dict):
    
    for tag in tags:
        tag_name = tag['name']
        output_dict.setdefault(tag_name,{})

        # goes through each file's json and name and adds them if they're not already in the comparison
        # If it's in the comparison but not because of the filename, it adds yes
        # otherwise it'll add no because the file did not have the tag_name
        for abbr,json in files.items():
            abbre = abbr.removesuffix('.json')
            
            if abbr in output_dict[tag_name]:
                print("skipped.")
                continue

            tag_in_json = any(tag.get("name") == tag_name for tag in json['containerVersion']['tag'])
            output_dict[tag_name][abbre] = "Yes" if tag_in_json else "No"

    return output_dict

def output_to_file(output_file:str,comparison_dict: dict[str,dict[str,str]]):
        with open(output_file,'w',encoding='utf-8') as file:
            
            for key,values in comparison_dict.items():
                # sets the empty text string that we fill
                text = "\t".join(values.values())
                #  loops through the list of copies and adds the addition 
                file.write(f"{key.strip('\n')}\t{text}\n")