import json
import os

def load_test_data(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    if os.path.getsize(file_path) == 0:
        raise ValueError(f"File is empty: {file_path}")
    
    with open(file_path, 'r') as file:
        return json.load(file)
