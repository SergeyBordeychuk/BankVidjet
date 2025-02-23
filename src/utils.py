import json
import os


def transaction_list(filename: str) -> list:
    relative_path = f"data/{filename}"
    absolute_path = os.path.abspath(relative_path)
    with open(absolute_path) as f:
        data = json.load(f)
    if data:
        return data
    return []
