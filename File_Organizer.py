#File_Organizer.py

###automate the organization of files on computer

import os
import shutil
from pathlib import Path
from datetime import datetime

def prompt_for_directory():
    """Prompt the user for the directory to organize."""
    directory_path = input("Please enter the directory path to organize: ")
    if not Path(directory_path).is_dir():
        print(f"The path {directory_path} is not a valid directory.")
        return None
    return Path(directory_path)

def classify_files(directory):
# Logic to classify files by type
    """Classify files in the directory by their file type (extension)."""
    file_mapping = {}
    for item in directory.iterdir():
        if item.is_file():
            file_type = item.suffix.lower() or "Other"
            if file_type not in file_mapping:
                file_mapping[file_type] = []
            file_mapping[file_type].append(item)
    return file_mapping
    
def create_folders(directory, categories):
    # Create folders for each category if they don't already exist
    
def move_files_to_folders(directory, file_mapping):
    # Move files to their respective folders based on the classification

def main():
    directory = Path("/path/to/directory")
    file_mapping = classify_files(directory)
    categories = file_mapping.keys()
    create_folders(directory, categories)
    move_files_to_folders(directory, file_mapping)

if __name__ == "__main__":
    main()