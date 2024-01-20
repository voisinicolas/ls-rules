import json


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


# Charger les données des deux fichiers JSON
with open("file1.json") as f1:
    data1 = json.load(f1)
with open("file2.json") as f2:
    data2 = json.load(f2)

# Fusionner les données
merged_data = merge_dicts(data1, data2)

# Écrire les données fusionnées dans un nouveau fichier JSON
with open("merged_file.json", "w") as f:
    json.dump(merged_data, f, indent=2)
