# What needs to happen:
# 1. get headers ready: tag name, trigger, each file name.
# 2. we open each file
# 3. we check if each name has already been found,
#    think of lowercase and random whitespaces.
# 4. if it has been found, check the country for yes
# 5. if it hasn't been found, check country for no.

# needs to return following schema:
# [
# tagname
# trigger
# filename1 value
# filename2 value
# filename3 value
# filename4 value
# ]
import os
import pathlib

from src.utils.jsonny import FileToJson as j_parse
from collections import defaultdict
from openpyxl import Workbook
from datetime import datetime



def get_file_names(filepaths: list[str]) -> dict[str, bool]:
    """
    Updates the headers global variable with all the filepaths.
    :param filepaths:
    :return: Updated global headers variable.
    """

    file_names = {}
    # adds all filenames into the header list. This will be used to add the check if they have it.
    for filepath in filepaths:
        filename = filepath.split("/")[-1].strip(".json")
        file_names[filename] = False
    return file_names


def compare(file_list: list[str], file_names: list[str]) -> dict[str, defaultdict]:
    # when adding a new record to this dict, it will give the file name dict as default value.
    holder = defaultdict(lambda: file_names.copy())

    for file in file_list:
        hi = str(file)
        print(hi)
        container_data = j_parse(hi)
        tags = container_data['containerVersion']['tag']

        # will update the holder dict.
        holder = check_tags(tags, holder, file)
    return holder


def check_tags(tags: list, holder_dict: defaultdict, file: str) -> defaultdict:
    """
    the way this works is that the default values for each dictionary item added
    is another dictionary item will all filenames empty.
    Thus it will still show false on all of them, but puts the ones it found to true.
    :param triggers: the list of triggers from the container
    :param tags: list of tags
    :param holder_dict: the dictionary that is holding the data outside this function
    :param file: the file that we are currently checken
    :return: a dict with a default value
    """
    file_name = file.split("/")[-1].strip(".json")
    print(file_name)

    # adds the tagname and set the filename to true.
    for tag in tags:
        tag_name = tag["name"].strip().lower()
        print("checking tag: ", tag_name)
        holder_dict[tag_name][file_name] = True
    return holder_dict


def to_report(file_paths: list[str], destination: str = "") -> None:
    # each file's name without the path or .json. We use it in the header.
    file_names = get_file_names(file_paths)
    print(file_names)

    # retrieves parsed data
    parsed_date = compare(file_paths, file_names)

    headers = ["Tag name"]

    # adds headers for each of the file names.
    for file_name in file_names.keys():
        headers.append(file_name)

    wb = Workbook()
    main = wb['Sheet']
    main.append(headers)

    for tag_name, data in parsed_date.items():
        formatted = [
            tag_name,
        ]
        for value in data.values():
            if value:
                formatted.append("true")
            else:
                formatted.append("false")

        main.append(formatted)

    main.column_dimensions["a"].width = 45

    now = datetime.now()
    wb.save(f"{destination}/comparison_{now.microsecond}{now.second}{now.minute}.xlsx")

