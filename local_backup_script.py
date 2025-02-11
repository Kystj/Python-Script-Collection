import os  # Interact with the operating system
import shutil  # Perform file and directory operations
import time  # Generate timestamps for backups
import argparse  # Parse the command-line arguments

# Define constants for backup management
MAX_BACKUP_LIFE = 30  # Maximum backup age in days
MAX_BACKUP_NUMBER = 5  # Keep only the last 5 backups

# Function to create a new backup
def create_backup(source_folder, backup_folder):
    timestamp = time.strftime('%Y_%m_%d')
    backup_name = f"backup_{timestamp}.zip"
    backup_path = os.path.join(backup_folder, backup_name)
    print(backup_path)

    # Create a ZIP archive of the source folder
    shutil.make_archive(backup_path.replace('.zip', ''), 'zip', source_folder)
    print(f"Backup created: {backup_path}")
    return backup_path

# Function to clean up old backups
def cleanup_backups(backup_folder):
    # Get a list of all backup files in the backup folder
    backup_files = [f for f in os.listdir(backup_folder) if f.endswith('.zip')]
    
    # Sort backups by modification time (oldest first)
    backup_files.sort(key=lambda f: os.path.getmtime(os.path.join(backup_folder, f)))

    # Remove backups older than MAX_BACKUP_LIFE days
    for b in backup_files:
        backup_path = os.path.join(backup_folder, b)
        backup_age_days = (time.time() - os.path.getmtime(backup_path)) / (60 * 60 * 24)  # Convert age to days

        if backup_age_days > MAX_BACKUP_LIFE:
            os.remove(backup_path)  # Delete the old backup
            print(f"Deleted old backup: {backup_path}")

    # Ensure only the last MAX_BACKUP_NUMBER backups are kept
    if len(backup_files) > MAX_BACKUP_NUMBER:
        files_to_remove = backup_files[:len(backup_files) - MAX_BACKUP_NUMBER]  # Get extra backups
        for f in files_to_remove:
            backup_path = os.path.join(backup_folder, f)
            os.remove(backup_path)  # Delete extra backups
            print(f"Deleted a backup to keep the last {MAX_BACKUP_NUMBER}: {backup_path}")

# Main function to parse arguments and execute backup tasks
def main():
    parser = argparse.ArgumentParser(description="Backup script with configurable source and destination folders.")
    parser.add_argument("source_folder", help="Path to the source folder to be backed up")  # Define source folder argument
    parser.add_argument("backup_folder", help="Path to the backup folder where backups will be stored")  # Define backup folder argument

    args = parser.parse_args()  # Parse command-line arguments

    cleanup_backups(args.backup_folder)  # Clean up old backups
    local_backup_path = create_backup(args.source_folder, args.backup_folder)  # Create a new backup

    print(f"Backup stored at: {local_backup_path}")

if __name__ == "__main__":
    main()

# Example:
# python backup_script.py "F:/Python/Scripts" "F:/Python/backup"
