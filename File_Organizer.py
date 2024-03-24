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

def classify_files_by_type(directory):
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
    
def create_folders_for_categories(directory, categories):
    """Create folders for each category if they don't already exist."""
    for category in categories:
        folder_path = directory / category.removeprefix(".")
        folder_path.mkdir(exist_ok=True)
    
def move_files(directory, file_mapping, dry_run=True):
    """Move files to their respective folders based on the classification."""
    log_entries = []
    for category, files in file_mapping.items():
        for file_path in files:
            new_path = directory / category.removeprefix(".") / file_path.name
            if dry_run:
                log_entries.append(f"DRY RUN: Would move {file_path} to {new_path}")
            else:
                shutil.move(str(file_path), str(new_path))
                log_entries.append(f"Moved {file_path} to {new_path}")
    return log_entries

def write_log(log_entries, directory):
    """Write the log entries to a log file in the specified directory."""
    log_file_path = directory / f"file_organizer_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    with log_file_path.open(mode='w') as log_file:
        for entry in log_entries:
            log_file.write(entry + "\n")
    print(f"Log file written to {log_file_path}")


def main():
    directory = Path("/path/to/directory")
    file_mapping = classify_files_by_type(directory)
    categories = file_mapping.keys()
    create_folders_for_categories(directory, categories)
    move_files(directory, file_mapping)

if __name__ == "__main__":
    main()