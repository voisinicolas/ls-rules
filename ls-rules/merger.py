import json

# Path to the collapsed JSON file
new_rules = './collapsed_data.json'
# Path to the old JSON file
old_path = './nvz-defaults-rules-temp.json'

# Function to append new rules to the old file
def append_to_old(old_path, new_rules):
    # Load the old and collapsed data

    with open(old_path, 'r') as file:
        old_data = json.load(file)
    with open(new_rules, 'r') as file:
        new_data = json.load(file)

    # Assuming both old_data and collapsed_data have a 'rules' key
    old_rules = old_data.get('rules', [])
    new_rules = new_data.get('rules', [])

    # Append new rules to the old rules
    old_rules.extend(new_rules)

  
# Save the updated data back to the old file
    with open(old_path, 'w') as file:
        json.dump(old_data, file, indent=2)


# Append the collapsed data to the old file
append_to_old(old_path, new_rules)

