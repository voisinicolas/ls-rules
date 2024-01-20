import json
import sys
import os
import tempfile
from cleaner2.py import collapse_array2


def collapse_array(data):
    collapsed = {}
    address_keys = ["remote-addresses", "remote-hosts", "remote"]

    for index, item in enumerate(data):
        try:
            address_key_found = None
            for address_key in address_keys:
                if address_key in item:
                    address_key_found = address_key
                    break

            direction = item.get("direction")
            ports = item.get("ports")
            action = item.get("action")
            process = item.get("process")
            protocol = item.get("protocol")
            key = (action, ports, direction, process, protocol, address_key_found)

            # Check if address_key_found exists in the item
            if address_key_found:
                remote_addresses = item.get(address_key_found)
                # if isinstance(remote_addresses, str):
                #         remote_addresses = [remote_addresses]  # Convert string to list
                if remote_addresses is not None:
                    if key not in collapsed:
                        collapsed[key] = item.copy()
                        # Initialize with a list containing the first address
                        collapsed[key][address_key_found] = [remote_addresses]
                    else:
                        if address_key_found not in collapsed[key]:
                            collapsed[key][address_key_found] = []
                        if isinstance(remote_addresses, list):
                            collapsed[key][address_key_found].extend(remote_addresses)
                        else:
                            collapsed[key][address_key_found].append(remote_addresses)
        except KeyError as e:
            print(f"Error occurred at rule index: {index}")
            print(f"Rule causing error: {item}")
            raise e
    return list(collapsed.values())


def process_collapsed_data(collapsed_data):
    for rule in collapsed_data:
        for key in ["remote-addresses", "remote-hosts", "remote"]:
            if key in rule and isinstance(rule[key], list) and len(rule[key]) == 1:
                # If there's only one entry in the list, replace the list with the single value
                rule[key] = rule[key][0]
    return collapsed_data


def is_valid_json(data):
    try:
        # Try serializing the data to a JSON string
        json.dumps(data)
        return data
    except (TypeError, OverflowError) as e:
        # If an error occurs during serialization, the data is not valid JSON
        print(f"Invalid JSON data: {e}")
        return False


def merger(data):
    return data


def main(file_path):
    # Read the JSON data from the file
    with open(file_path, "r") as file:
        json_data = json.load(file)

    rules = json_data["rules"]
    collapsed_data = collapse_array2(rules)
    cleaned_data = process_collapsed_data(collapsed_data)
    is_valid_data = is_valid_json(cleaned_data)

    file_name = os.path.splitext(os.path.basename(file_path))[0]

    final_output = {
        "description": "NVZ Litte Snitch Rules file",
        "name": file_name,
        "rules": is_valid_data,  # assuming processed_data is a list of rules
    }
    # Print or save the collapsed data
    # print(json.dumps(collapsed_data, indent=4))
    # Optionally, save the result to a file
    with open(file_path, "w") as file:
        json.dump(final_output, file, indent=2)

    with tempfile.NamedTemporaryFile(mode="w", delete=False) as temp_file:
        json.dump(final_output, temp_file, indent=2)
        temp_file_path = temp_file.name

    # Safely replace the old file with the new file
    os.replace(temp_file_path, file_path)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    main(file_path)
