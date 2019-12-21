import os
from pathlib import Path


def get_input_file(file_name: str):
    path_to_current_file = os.path.realpath(__file__)
    current_directory = os.path.split(path_to_current_file)[0]
    data_folder = Path(current_directory).parent.parent / "inputData/" / file_name
    return data_folder