
import json
import sys

def format_json_file(file_path):
    try:
        # Read the existing content of the file
        with open(file_path, 'r') as file:
            data = json.load(file)

        # Write back the formatted JSON
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=2) # You can change the indent level as needed

        print(f"Formatted file: {file_path}")
    except Exception as e:
        print(f"An error occurred with file {file_path}: {e}")

if __name__ == "__main__":
    # Loop over each argument (excluding the script name itself)
    for file_path in sys.argv[1:]:
        format_json_file(file_path)
