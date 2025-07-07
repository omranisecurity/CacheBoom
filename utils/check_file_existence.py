import os

def check_file_existence(file_path: str) -> bool:
    return os.path.isfile(file_path)