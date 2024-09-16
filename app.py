import os
import random
import string
import json

# Function to generate a random 16-character alphanumeric string
def generate_random_hash():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=16))

# Function to check if a file is an image
def is_image(file_name):
    valid_extensions = ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp')
    return file_name.lower().endswith(valid_extensions)

# Read the current directory
current_directory = os.path.dirname(os.path.abspath(__file__))
json_output = {}

# Iterate through all files in the directory
for file_name in os.listdir(current_directory):
    try:
        # If the file is an image
        if is_image(file_name):
            # Generate a random hash for the new name
            new_name = generate_random_hash() + os.path.splitext(file_name)[1]

            # Get the full file paths
            old_file_path = os.path.join(current_directory, file_name)
            new_file_path = os.path.join(current_directory, new_name)

            # Rename the file
            os.rename(old_file_path, new_file_path)

            # Store the old and new names in the dictionary
            json_output[file_name] = new_name

    except Exception as e:
        print(f"Error processing file '{file_name}': {e}")

# Save the old and new names in a JSON file
try:
    with open('image_renames.json', 'w') as json_file:
        json.dump(json_output, json_file, indent=4)
    print(f"Renaming complete. Original and new names stored in 'image_renames.json'.")
except Exception as e:
    print(f"Error writing JSON file: {e}")
