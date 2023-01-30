from gendiff.parser import pair_files_loader
from gendiff.diff import diff_mapping
from gendiff.formatters.stylish import stylish
from gendiff.formatters.plain import plain
from gendiff.formatters.json import to_json


FORMATS = {
    'stylish': stylish,
    'plain': plain,
    'json': to_json
}


def generate_diff(file1, file2, format='stylish'):

    dict1, dict2 = pair_files_loader(file1, file2)
    mapping = diff_mapping(dict1, dict2)
    result = FORMATS[format](mapping)
    return result
