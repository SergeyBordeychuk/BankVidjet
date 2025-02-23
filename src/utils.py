import json
import os

relative_path = "data/"
absolute_path = os.path.abspath(relative_path)

def transaction_list(filename: str) -> list:
    with open(f'{absolute_path}\{filename}') as f:
        data = json.load(f)
    if data:
        return data
    return []
