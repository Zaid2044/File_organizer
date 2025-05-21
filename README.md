# Automated File Organizer

A Python script to automatically organize files in a specified directory into subdirectories based on their file extensions. Organization rules are defined in an external JSON configuration file.

## Features

*   Organizes files into subdirectories based on their extension (e.g., `.pdf` files into a "PDFs" folder).
*   User-configurable mappings via an external JSON file (`organizer_config.json` by default).
*   The source directory to be organized is specified as a command-line argument.
*   Automatically creates target subdirectories if they don't already exist.
*   Files with extensions not defined in the configuration are moved to a default "Others" folder.
*   Provides feedback on files moved and basic error handling.

## Requirements

*   Python 3.6+ (primarily uses standard library features common in most Python 3 versions).
*   No external non-standard libraries are required.

## Setup & Configuration

1.  **Configuration File:**
    The script uses a JSON file to define how file extensions map to target folder names. By default, it looks for `organizer_config.json` in the same directory as the script.

    An example `organizer_config.json` might look like this:
    ```json
    {
      ".pdf": "PDFs",
      ".jpg": "Images",
      ".jpeg": "Images",
      ".png": "Images",
      ".txt": "TextFiles",
      ".docx": "Documents",
      ".zip": "Archives",
      ".csv": "Data",
      ".py": "PythonScripts",
      ".mp3": "Music",
      ".mp4": "Videos",
      ".exe": "Executables",
      ".iso": "DiskImages"
    }
    ```
    *   You can customize this file to add new rules or change existing ones.
    *   The **keys** are the file extensions (including the leading dot, lowercase).
    *   The **values** are the names of the subdirectories where corresponding files will be moved.

2.  **Ensure `organizer.py` and your configuration file (e.g., `organizer_config.json`) are accessible.**

## Usage

To run the script, open your terminal or command prompt, navigate to the directory containing `organizer.py`, and use the following command structure:

```bash
python organizer.py <path_to_directory_to_organize>


Arguments:

<path_to_directory_to_organize>: (Required) The full or relative path to the directory whose files you want to organize.

Optional Arguments:

-c <path_to_config_file> or --config <path_to_config_file>:
Allows you to specify a custom path to the JSON configuration file. If not provided, it defaults to organizer_config.json in the script's directory.

Examples:

Organize files in a directory named Downloads located in your user's home folder (assuming organizer.py is elsewhere):

python organizer.py /Users/yourusername/Downloads
IGNORE_WHEN_COPYING_START
content_copy
download
Use code with caution.
Bash
IGNORE_WHEN_COPYING_END

(On Windows, this might be python organizer.py C:\Users\yourusername\Downloads)

Organize files in a subdirectory named messy_folder relative to where you are running the script:

python organizer.py ./messy_folder
IGNORE_WHEN_COPYING_START
content_copy
download
Use code with caution.
Bash
IGNORE_WHEN_COPYING_END

Organize files using a custom configuration file named my_rules.json:

python organizer.py ./messy_folder -c ./my_rules.json
IGNORE_WHEN_COPYING_START
content_copy
download
Use code with caution.
Bash
IGNORE_WHEN_COPYING_END
How It Works

The script reads the specified source directory.

It loads file extension mappings from the JSON configuration file.

For each file in the source directory:

It extracts the file extension.

It determines the target subdirectory based on the loaded mappings. If an extension is not found in the mappings, it defaults to an "Others" folder.

It creates the target subdirectory within the source directory if it doesn't already exist.

It moves the file into the appropriate target subdirectory.

The script prints a summary of actions taken or any errors encountered.

Future Improvements (TODO)

Implement a "dry run" mode to preview changes without actually moving files.

Add more robust logging using Python's logging module, with options to log to a file.

Implement advanced file collision handling (e.g., renaming files if a file with the same name already exists in the target directory).

Allow specifying a separate base destination directory (instead of creating subfolders within the source directory).

Add support for organizing based on more complex rules (e.g., filenames, date created).

---
