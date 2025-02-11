# Python-Script-Collection
## Overview

This collection includes a variety of Python scripts for different use cases.

Each script is independent and intended to perform specific tasks. You can choose and run only the scripts that meet your needs.

## Table of Contents
- [Network Scanner Script](#network-scanner)

# Network Scanner Script

### Overview


### Features


### Requirements


### Usage Instructions

# Local Backup Script

### Overview

This Python script creates compressed backups of a specified folder and manages backup retention by deleting old backups based on age and count limits. It allows users to specify the source folder and backup destination via command-line arguments.

# Features

    Automatically creates ZIP archives of a specified folder.
    Uses timestamps in the format YYYY_MM_DD_HHMMSS for organized backups.
    Deletes backups older than a defined number of days (MAX_BACKUP_LIFE).
    Limits the number of stored backups to the latest (MAX_BACKUP_NUMBER).
    Fully configurable via command-line arguments.

# Requirements

    Python 3.x
    Required modules (pre-installed in most Python versions):
        os – for interacting with the file system
        shutil – for file operations and ZIP creation
        time – for generating timestamps
        argparse – for parsing command-line arguments

# Usage Instructions

    Open a terminal or command prompt.
    Run the script with the following format:

    python backup_script.py <source_folder> <backup_folder>

Example:

    python backup_script.py "F:/Python/Scripts" "F:/Python/backup"

    The script will:
        Clean up old backups based on age and count settings.
        Create a new compressed backup in the specified backup folder.
        Print the backup location.

Example Output

F:/Python/backup/backup_2025_02_11_153045.zip  
Backup created: F:/Python/backup/backup_2025_02_11_153045.zip  
Backup stored at: F:/Python/backup/backup_2025_02_11_153045.zip 
