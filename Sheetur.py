from convert_sheet import FileToJson
import os
# Sheetur is used to compare GTM containers.


# The idea is that we open all files and put them in a dict.
# We go through each .json file
# If we find a tag that we don't have yet, we add it, and a prefix.
# If we do have it, add the tag.
# If we don't have it in our main file, and we do have it in our dict, add a -.
def Compare_sheets(folder_path:str): 
    jsonFiles = {}
    comparison = {}
    
    # Loops through each file and 
    # returns each respective json file under their adverb
    for file in os.listdir(folder_path):
        name = file.split("_")[1]
        jsonFiles[name] = FileToJson(folder_path+"/"+file)
    
    # loop through each file. and gets a list of tags and triggers.
    for name, json in jsonFiles.items():
        tags = json['containerVersion']['tag']

        # Loops through all tags
        comparison = compare_tag_to_files(tags,jsonFiles,comparison)
        output_to_file('compared_sheets/output.txt',comparison)

def compare_tag_to_files(tags:list[str],files: dict, output_dict:dict):
    comparedTags = output_dict

    for tag in tags:
        tag_name = tag['name']
        for abbr,json in files.items():
            abbre = abbr.strip('.json')
            print(f"checking {tag_name} in {abbr}...")
            
            # some rules for the compared_tags
            
            # if tag name not compared and in the other file
            if tag_name not in comparedTags and any(tag.get("name") == tag_name for tag in json['containerVersion']['tag']):
                comparedTags[tag_name] = [abbre]

            elif tag_name in comparedTags and abbre in comparedTags[tag_name]:
                print("skipped")

            # if the tagname is in btoh files but no abbreviation
            elif tag_name in comparedTags and any(tag.get("name") == tag_name for tag in json['containerVersion']['tag']):
                comparedTags[tag_name].append(abbre)


            # if compared
            elif tag_name in comparedTags and not any(tag.get("name") == tag_name for tag in json['containerVersion']['tag']):
                comparedTags[tag_name].append(" - ")


    print(comparedTags)
    return comparedTags

def output_to_file(output_file:str,comparison_dict: dict[str,list[str]]):
        with open(output_file,'w',encoding='utf-8') as file:
            for key,values in comparison_dict.items():
                # sets the empty text string that we fill
                text = "\t".join(values)
                #  loops through the list of copies and adds the addition 
                file.write(f"{key.strip('\n')}\t{text}\n")