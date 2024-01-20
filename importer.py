import os
import json
import sys


def find_matching_file(filename, directory):
    for file in os.listdir(directory):
        if file == filename:
            return os.path.join(directory, file)
    return None


def merge_dicts(dict1, dict2):
    merged = dict()

    for key in dict1:
        if key in dict2:
            if isinstance(dict1[key], dict) and isinstance(dict2[key], dict):
                merged[key] = merge_dicts(dict1[key], dict2[key])
            elif isinstance(dict1[key], list) and isinstance(dict2[key], list):
                merged[key] = dict1[key] + dict2[key]
            else:
                merged[key] = dict2[key]
        else:
            merged[key] = dict1[key]

    for key in dict2:
        if key not in merged:
            merged[key] = dict2[key]
    return merged


# Command-line arguments
if len(sys.argv) != 2:
    print("Usage: script.py <new_data_file.json>")
    sys.exit(1)

new_data_file = sys.argv[1]

target_directory = "/Users/nvz/.config/little-snitch/ls-rules/"
filename, file_extension = os.path.splitext(os.path.basename(new_data_file))
filename = filename + file_extension
old_data_file = find_matching_file(filename, target_directory)
target_file = target_directory + filename
# Charger les données des deux fichiers JSON
print(target_file)
with open(new_data_file) as f1:
    data1 = json.load(f1)

if old_data_file is not None:
    with open(old_data_file) as f2:
        data2 = json.load(f2)

    merged_data = merge_dicts(data1, data2)
    print(merged_data)
    with open(target_file, "w") as file:
        json.dump(merged_data, file, indent=2)

else:
    with open(target_file, "w") as file:
        json.dump(data1, file, indent=2)
