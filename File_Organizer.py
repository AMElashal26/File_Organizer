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