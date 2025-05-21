import os
import shutil
import argparse
import json

DEFAULT_MAPPINGS = { 
    ".other": "Others" 
}

def load_mappings(config_path="organizer_config.json"):
    try:
        with open(config_path, 'r') as f:
            mappings = json.load(f)
        print(f"Successfully loaded mappings from {config_path}")
        return mappings
    except FileNotFoundError:
        print(f"Warning: Configuration file '{config_path}' not found. Using default 'Others' mapping for unknown types.")
        return DEFAULT_MAPPINGS 
    except json.JSONDecodeError:
        print(f"Warning: Error decoding JSON from '{config_path}'. Is it valid JSON? Using default 'Others' mapping.")
        return DEFAULT_MAPPINGS
    except Exception as e:
        print(f"Warning: An unexpected error occurred loading '{config_path}': {e}. Using default 'Others' mapping.")
        return DEFAULT_MAPPINGS
    

def organize_files(directory_to_scan, file_mappings):
    print(f"Scanning directory: {directory_to_scan}")
    try:
        items_in_directory = os.listdir(directory_to_scan)
    except FileNotFoundError:
        print(f"Error: Directory not found at {directory_to_scan}")
        return
    except Exception as e:
        print(f"Error listing directory {directory_to_scan}: {e}")
        return

    print("\nProcessing files:")
    files_moved_count = 0
    for item_name in items_in_directory:
        full_item_path = os.path.join(directory_to_scan, item_name)

        if os.path.isfile(full_item_path):
            filename, file_extension = os.path.splitext(full_item_path)
            file_extension = file_extension.lower()

            target_folder_name = file_mappings.get(file_extension, "Others")
            
            full_target_folder_path = os.path.join(directory_to_scan, target_folder_name)
            
            try:
                os.makedirs(full_target_folder_path, exist_ok=True)
            except Exception as e:
                print(f"Error creating directory {full_target_folder_path}: {e}")
                continue

            destination_file_path = os.path.join(full_target_folder_path, item_name)

            try:
                shutil.move(full_item_path, destination_file_path)
                print(f"Moved: {item_name} -> {target_folder_name}/")
                files_moved_count += 1
            except Exception as e:
                print(f"Error moving {item_name}: {e}")

    if files_moved_count == 0 and not items_in_directory:
        print("No files found in the directory to organize.")
    elif files_moved_count == 0 and items_in_directory:
        print("No files were moved (perhaps they were already organized or are directories).")
    else:
        print(f"\nSuccessfully moved {files_moved_count} file(s).")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Organize files in a directory by their extension.")
    parser.add_argument("source_directory_arg",
                        help="The directory containing files to organize.")
    parser.add_argument("-c", "--config", default="organizer_config.json",
                        help="Path to the JSON configuration file for mappings (default: organizer_config.json)")

    args = parser.parse_args()
    current_file_mappings = load_mappings(args.config)

    directory_to_process = args.source_directory_arg
    organize_files(directory_to_process, current_file_mappings)