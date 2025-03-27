import csv
import pandas as pd
from src.utils.jsonny import FileToJson as j_parse

def convert_to_csv(filepaths: list[str],destination: str) -> None:
    headers = ["Tag name",
               "Category",
               "Sends to",
               "Triggers",
               "Requires consent",
               "Comment"]

    sheets_dict = files_to_data(filepaths)




def files_to_data(filepaths)->dict[str, dict]:
    data_sheets = {}

    # Goes through each file to read the container tag data.
    for file_path in filepaths:
        gtm_container = j_parse(file_path)
        container_name = gtm_container['containerVersion']['container']['name']
        print(container_name)
        tags = gtm_container['containerVersion']['tag']
        triggers = gtm_container['containerVersion']['trigger']

        # creates a list of all tags ordered in a nice associated array.
        sheet_rows = list(map(lambda tag: process_tag(tag,triggers),tags))
        data_sheets[container_name] = sheet_rows
    return data_sheets


def process_tag(tag,triggers):
    event = confirm_event(tag['type'])
    return {
        "Tag name": tag['name'],
        "Category": event,
        "Sends to": sends_to(event),
        "Triggers": get_trigger_name(tag['firingTriggerId'], triggers),
        "Requires consent": is_consent_needed(tag['consentSettings']['consentStatus']),
        "Comment": get_additional_info(tag)
    }

# Outputs a file from imports to exports to use in a table.
# def OutputToFile (fileName):
#     data = FileToJson("./JSON_imports/"+fileName)
#
#     tags = data['containerVersion']['tag']
#     triggers = data['containerVersion']['trigger']
#
#     print("Exporting table...")
#     total = 0
#     with open("./JSON_outputs/"+fileName.strip('.json')+"_SHEETABLE.txt", "w") as output:
#         for tag in tags:
#
#             if 'firingTriggerId' not in tag:
#                 tag['firingTriggerId'] = "All pages"
#
#             event = confirmEvent(tag['type'])
#             output.write(f"{tag['name']}\t{event}\t{SendsTo(event)}\t{GetTriggerName(tag['firingTriggerId'],triggers)}\t{isConsentNeeded(tag['consentSettings']['consentStatus'])}\t{getAdditionalInfo(tag)}\t\n")
#             total = total + 1
#     print(f"done! {total} tags found and extracted.")


def confirm_event(name):
    if name == "gaawe":
        return "Google analytics"
    elif name == "html":
        return "Custom HTML"
    elif name == "cvt_166370652_63":
        return "Facebook pixel"
    elif name in ["awct", "gclidw", "sp"]:
        return "Google Ads"
    elif name == "googtag":
        return "google tag"
    else:
        return name


def get_trigger_name(trigger_IDs, triggers):
    if trigger_IDs is None:
        return "no trigger"

    for triggerID in trigger_IDs:
        for trigger in triggers:
            if trigger['triggerId'] == triggerID:
                return trigger['name']
        return "All pages"


def is_consent_needed(consent):
    if consent == "NOT_SET":
        return "No (not set)"
    elif consent == "NEEDED":
        return "Required"


def sends_to(category):
    if category == "Custom HTML":
        return "Datalayer"
    else:
        return category

def get_additional_info(tag):
    response = ""
    if 'paused' in tag and tag['paused'] == True:
        response += "paused"
    return response