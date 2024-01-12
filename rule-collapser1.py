import json
import sys


def collapse_array(data):
    collapsed = {}
    for item in data:
        key = (item['action'], item['ports'],
               item['process'], item['protocol'])

        # Check if 'remote-hosts' exists in the item
        remote_addresses = item.get('remote-hosts')
        if remote_addresses is not None:
            if key not in collapsed:
                collapsed[key] = item.copy()
                # Initialize with a list containing the first address
                collapsed[key]['remote-hosts'] = [remote_addresses]
            else:
                # Append to the existing list
                collapsed[key]['remote-hosts'].append(remote_addresses)

    return list(collapsed.values())


def main(file_path):
    # Read the JSON data from the file
    with open(file_path, 'r') as file:
        json_data = json.load(file)
        rules = json_data["rules"]
        collapsed_data = collapse_array(rules)

    # Print or save the collapsed data
    # print(json.dumps(collapsed_data, indent=4))
    # Optionally, save the result to a file
    with open('collapsed_data1.json', 'w') as file:
        json.dump(collapsed_data, file, indent=4)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    main(file_path)
