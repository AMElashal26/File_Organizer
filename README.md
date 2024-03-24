 #file organizer

This is an automation project processing different types of files. 

This script classifies files by type, creates folders for each file type, and moves files into their designated folders. It features a dry run mode to preview actions without making changes and generates a log file detailing the script's actions for transparency and audit purposes.

### Key Components of the Script:
* Directory Input: The script prompts the user to enter the directory path they want to organize.
* File Classification: Files are classified by their extension into different categories.
* Folder Creation: Folders are created for each file category, if they don't already exist.
* File Moving: Files are moved to their respective category folders. A dry run option allows previewing these actions without executing them.
* Logging: Actions taken by the script are logged into a file within the same directory, providing a record of changes.