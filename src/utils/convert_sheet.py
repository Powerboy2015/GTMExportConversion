import csv
import pandas as pd
from openpyxl import Workbook
from openpyxl.styles import Font
from src.utils.jsonny import FileToJson as j_parse
from datetime import datetime

def convert_to_csv(filepaths: list[str],destination: str ="") -> None:
    headers = ["Tag name",
               "Category",
               "Sends to",
               "Triggers",
               "Requires consent",
               "Comment"]

    sheets_dict = files_to_data(filepaths)

    wb = Workbook()
    for sheet,tags in sheets_dict.items():
        sheet_obj = wb.create_sheet(title=sheet)

        sheet_obj.append(headers)

        for tag in tags:
            print(tag)
            sheet_obj.append(tag)

        sheet_obj.column_dimensions["a"].width = 45
        sheet_obj.column_dimensions["b"].width = 20
        sheet_obj.column_dimensions["c"].width = 20
        sheet_obj.column_dimensions["d"].width = 40
        sheet_obj.column_dimensions["e"].width = 15
        sheet_obj.column_dimensions["f"].width = 10

        sheet_obj.freeze_panes = sheet_obj['A2']

        for cell in sheet_obj[1]:
            cell.font = Font(bold=True)

    now = datetime.now()

    wb.save(f"{destination}/output_{now.microsecond}{now.second}{now.minute}.xlsx")


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


def process_tag(tag: dict[str,str],triggers):
    event = confirm_event(tag['type'])
    trigger_id = tag.get("firingTriggerId") or ""
    print(tag['name'])
    return [
        tag['name'] or "",
        event or "",
        sends_to(event) or "",
        get_trigger_name(trigger_id or "", triggers) or "",
        is_consent_needed(tag['consentSettings']['consentStatus']) or "",
        get_additional_info(tag) or ""
    ]


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
    return "not required"


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