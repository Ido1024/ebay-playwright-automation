import json
import os


def load_test_data(key: str):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, "..", "data", "search_data.json")

    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data.get(key)
