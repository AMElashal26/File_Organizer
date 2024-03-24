 #file organizer

This is an automation project processing different types of files. 

This script classifies files by type, creates folders for each file type, and moves files into their designated folders. It features a dry run mode to preview actions without making changes and generates a log file detailing the script's actions for transparency and audit purposes.

### Key Components of the Script:
* Directory Input: The script prompts the user to enter the directory path they want to organize.
* File Classification: Files are classified by their extension into different categories.
* Folder Creation: Folders are created for each file category, if they don't already exist.
* File Moving: Files are moved to their respective category folders. A dry run option allows previewing these actions without executing them.
* Log File: Generate a log file detailing the actions taken (files moved, folders created, etc.). This can be useful for auditing and understanding what the script did.
* Dry Run Mode: Implement a mode where the script simulates its actions (showing what it would do) without actually moving or altering files. This feature lets users see what changes will occur before committing to them.


