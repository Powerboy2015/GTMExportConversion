import os
import json
import re

def confirmEvent(name):
    if name == "gaawe":
        return "Google analytics"
    elif name == "html":
        return "Custom HTML"
    elif name == "cvt_166370652_63":
        return "Facebook pixel"
    elif name in ["awct","gclidw","sp"]:
        return "Google Ads"
    elif name == "googtag":
        return "google tag"
    else:
        return name
    
def GetTriggerName(triggerIDs,triggers):
    if triggerIDs == None:
        return "no trigger"

    for triggerID in triggerIDs:
            for trigger in triggers:
                if trigger['triggerId'] == triggerID:
                    return trigger['name']
            return "All pages"
                
def isConsentNeeded(consent):
    if consent == "NOT_SET":
        return "No (not set)"
    elif consent == "NEEDED":
        return "Required"

def SendsTo(category):
    if category == "Custom HTML":
        return "Datalayer"
    else:
        return category
    

    
def getAdditionalInfo(tag):
    response = ""
    if 'paused' in tag and tag['paused'] == True:
        response += "paused"
    return response


# Gets a file and returns it as a json
def FileToJson(filepath):
    print("getting file...")
    with open(filepath, 'r', encoding='utf-8-sig') as file:
        content = file.read()
        print("contents read!")
    # Now try parsing
    try:
        print("getting json...")
        return json.loads(content)
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON: {e}")

# Outputs a file from imports to exports to use in a table.
def OutputToFile (fileName):
    data = FileToJson("./JSON_imports/"+fileName)

    tags = data['containerVersion']['tag']
    triggers = data['containerVersion']['trigger']

    print("Exporting table...")
    total = 0
    with open("./JSON_outputs/"+fileName.strip('.json')+"_SHEETABLE.txt", "w") as output:
        for tag in tags:
        
            if 'firingTriggerId' not in tag:
                tag['firingTriggerId'] = "All pages"
        
            event = confirmEvent(tag['type'])
            output.write(f"{tag['name']}\t{event}\t{SendsTo(event)}\t{GetTriggerName(tag['firingTriggerId'],triggers)}\t{isConsentNeeded(tag['consentSettings']['consentStatus'])}\t{getAdditionalInfo(tag)}\n")
            total = total + 1
    print(f"done! {total} tags found and extracted.")

def CompareToFound(NewFile):
    data = FileToJson("./JSON_imports/"+NewFile)
    with open("compared.txt", "r+") as file:
        fileContents = file.readlines()

        for tag in data['containerVersion']['tag']:
            tag_name = tag['name'].strip()  # Strip leading/trailing spaces from tag['name']

            pattern = re.compile(tag_name)
            
            for idx, line in enumerate(fileContents):
                match = pattern.match(line.strip())  # Match the start of the line with the regex pattern
                if match and match.group(1) == tag_name:
                    # If the tag_name already exists, append " - duplicate" to it
                    fileContents[idx] = f"{line.strip()} - {NewFile.strip(".json")}\n"
                else:
                    fileContents.append(tag_name+"\n")
                break
        file.writelines(fileContents)

                

# Gets all my sheetsx
files = [f for f in os.listdir("./JSON_imports") if os.path.isfile(os.path.join("./JSON_imports", f))]
for file in files:
    OutputToFile(file)

# compares all the files to 
extractedfiles = [f for f in os.listdir("./JSON_imports") if os.path.isfile(os.path.join("./JSON_imports", f))]
for file in extractedfiles:
    CompareToFound(file)