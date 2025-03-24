import json


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