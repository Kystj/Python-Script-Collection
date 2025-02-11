# Python-Script-Collection
## Overview

This collection includes a variety of Python scripts for different use cases.

Each script is independent and intended to perform specific tasks. You can choose and run only the scripts that meet your needs.

## Table of Contents
- [Network Scanner Script](#network-scanner)
- [Local Backup Script](#local-backup-script)

# Network Scanner Script

##Overview

This Python script scans a local network to identify active devices and checks for open ports on each detected device. It uses multithreading to speed up the scanning process and is compatible with multiple operating systems.

#Features

    Automatically detects the local network subnet.
    Scans the network for active devices.
    Identifies open ports on discovered devices.
    Uses multithreading for faster scanning.
    Compatible with Windows and Linux/macOS.

#Requirements

    Python 3.x
    Required modules (pre-installed in most Python versions):
        socket – for network communication
        subprocess – for executing ping commands
        ipaddress – for handling subnet calculations
        platform – for OS detection
        concurrent.futures.ThreadPoolExecutor – for multithreading

#Usage Instructions

    Open a terminal or command prompt.
    Run the script:

    python network_scanner.py

    The script will:
        Detect the local subnet.
        Ping all IPs in the subnet to find active devices.
        Scan common ports (22, 80, 443, 3389, 8080) on each active device.
        Display a list of discovered devices and their open ports.

    Example Output

    Scanning network: 192.168.1.0/24 ...
    
    Devices Found:
    IP: 192.168.1.10, Open Ports: [22, 80]
    IP: 192.168.1.15, Open Ports: [443, 3389]

# Local Backup Script

### Overview

This Python script creates compressed backups of a specified folder and manages backup retention by deleting old backups based on age and count limits. It allows users to specify the source folder and backup destination via command-line arguments.

# Features

    Automatically creates .zip archives of a specified folder.
    Uses timestamps in the format YYYY_MM_DD for organized backups.
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

    Example Output

    python backup_script.py "F:/Python/Scripts" "F:/Python/backup"

    F:/Python/backup/backup_2025_02_11_153045.zip  
    Backup created: F:/Python/backup/backup_2025_02_11_153045.zip  
    Backup stored at: F:/Python/backup/backup_2025_02_11_153045.zip 
