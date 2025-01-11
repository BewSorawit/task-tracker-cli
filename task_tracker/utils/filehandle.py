import json
import os
from typing import List

class FileHandle:
    def __init__(self, filename: str):
        self.filename = filename

    def write_file(self, json_object:object):
        try:
            with open(self.filename, "w") as file:
                json.dump(json_object, file, indent=4)
        except Exception as e:
            print(f"Error writing to file: {e}")

    def read_file(self) -> List[dict]:
        try:
            if not os.path.isfile(self.filename):
                return []
            with open(self.filename) as file:
                return json.load(file)
        except Exception as e:
            print(f"Error reading file: {e}")
            return []