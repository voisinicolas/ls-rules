import json

# Path to the collapsed JSON file
new_rules = './proton.json'
# Path to the master JSON file
master_path = './nvz-defaults-rules.json'

# Function to append new rules to the master file
def append_to_master(master_path, new_rules):
    # Load the master and collapsed data

    with open(master_path, 'r') as file:
        master_data = json.load(file)
    with open(new_rules, 'r') as file:
        new_rules_data = json.load(file)

    # Assuming both master_data and collapsed_data have a 'rules' key
    master_rules = master_data.get('rules', [])
    new_rules = new_rules_data.get('rules', [])

    # Append new rules to the master rules
    master_rules.extend(new_rules)

  
# Save the updated data back to the master file
    with open(master_path, 'w') as file:
        json.dump(master_data, file, indent=2)


# Append the collapsed data to the master file
append_to_master(master_path, new_rules)

