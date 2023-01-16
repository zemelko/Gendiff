import pathlib
import json
import yaml


def pair_files_loader(file1, file2):

    YAML = {'.yml', '.yaml'}
    JSON = {'.json'}

    left_dict = {}
    right_dict = {}
    extension_file1 = pathlib.Path(file1).suffix
    extension_file2 = pathlib.Path(file2).suffix

    if extension_file1 == extension_file2:
        extension = extension_file1 = extension_file2

    if extension in YAML:
        left_dict = yaml.safe_load(open(file1))
        right_dict = yaml.safe_load(open(file2))
    elif extension in JSON:
        left_dict = json.load(open(file1))
        right_dict = json.load(open(file2))

    return [left_dict, right_dict]