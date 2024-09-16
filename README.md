# Image Renamer Script

## Overview

This Python script renames all image files in the current directory to a random 16-character alphanumeric string. It then stores the original filenames and their new names in a JSON file for reference. This is useful for anonymizing or obfuscating image filenames.

## Features

- **Random Renaming:** Each image file is renamed to a unique 16-character alphanumeric string.
- **JSON Record:** The original and new filenames are recorded in a `image_renames.json` file.
- **Error Handling:** The script includes error handling to ensure that errors with individual files do not stop the entire process.

## Requirements

- Python 3.x
- No external libraries required

## Usage

1. **Place the Script:**
   - Save the script in the directory containing the image files you want to rename.

2. **Run the Script:**
   - Open a terminal or command prompt.
   - Navigate to the directory where the script is located.
   - Run the script using Python:

     ```bash
     python app.py
     ```

3. **Check the Results:**
   - The script will rename all image files in the directory.
   - The original and new filenames will be saved in a file named `image_renames.json` in the same directory.

## Example

### Before Running

Assume you have the following image files in your directory:

- `photo1.jpg`
- `vacation.png`

### After Running

The files will be renamed to something like:

- `A1b2C3d4E5F6G7H8.jpg`
- `9I0jK1L2mN3O4P5.png`

And `image_renames.json` will contain:

```json
{
    "photo1.jpg": "A1b2C3d4E5F6G7H8.jpg",
    "vacation.png": "9I0jK1L2mN3O4P5.png"
}
```

## Error Handling

- The script reports errors if a file cannot be processed and continues with the remaining files.
- Errors in writing the JSON file are also reported.

## License

This script is provided under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contributing

Feel free to open an issue or submit a pull request if you have suggestions or improvements.
