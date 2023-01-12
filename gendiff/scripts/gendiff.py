import argparse
from itertools import chain
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

  
def generate_diff(file1, file2):
  
  dict1, dict2 = pair_files_loader(file1, file2)

  
  def diff(d1, d2):

    union_keys = d1.keys() | d2.keys()
    
    intersection_keys = d1.keys() & d2.keys()
    left = d1.keys() - d2.keys()
    right = d2.keys() - d1.keys()
    
    sorted_union_keys = sorted(union_keys)
    lines = []
  
    def parsed_value(value):  
      if isinstance(value, bool):
        if value == True:
          return 'true'
        else:
          return 'false'
      elif value == None:
        return 'null'
      else:
        return value
        
    def get_line(key):
  
      left_value = parsed_value(d1.get(key))
      right_value = parsed_value(d2.get(key))
      
      ind_default = '  '
      ind_both = '  '

      value = left_value if left_value == right_value else ''
        
      ind_left = '- '
      ind_right = '+ '
        
      if key in intersection_keys:
        
        if left_value == right_value:
          return f'{ind_default}{ind_both}{key}: {value}'
        else:
          return f'{ind_default}{ind_left}{key}: {left_value}\n{ind_default}{ind_right}{key}: {right_value}'
      if key in left:
          return f'{ind_default}{ind_left}{key}: {left_value}'
      if key in right:
          return f'{ind_default}{ind_right}{key}: {right_value}'
  
    lines = list(map(get_line, sorted_union_keys))
      
    files_diff =  '\n'.join(chain('{', lines, '}'))
  
    return files_diff

  return diff(dict1, dict2)

  
def main():

  parser = argparse.ArgumentParser(description='Compares two   configuration files and whows a difference.')

  parser.add_argument('-f', '--format', help='set format of output')
  parser.add_argument('file_1', metavar='first_file')
  parser.add_argument('file_2', metavar='second_file')

  args = parser.parse_args()
  result = generate_diff(args.file_1, args.file_2)
  print(result)


if __name__ == '__main__':
  main()