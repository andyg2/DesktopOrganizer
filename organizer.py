import os
import shutil
import datetime
from config import get_extension_directory_map, get_default_directory

def organize_files(base_directory):
    # Get the list of files on the desktop
    files = os.listdir(base_directory)
    
    # Get the current timestamp
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")

    for file in files:
        file_path = os.path.join(base_directory, file)

        # Check if the item is a file
        if os.path.isfile(file_path):
            file_extension = os.path.splitext(file)[1].lower()

            # Create the destination directory based on file extension
            destination_directory = get_destination_directory(file_extension, base_directory)

            # Create the directory if it doesn't exist
            if not os.path.exists(destination_directory):
                os.makedirs(destination_directory)

            # Move the file to the destination directory
            try:
                shutil.move(file_path, destination_directory)
                print(f"Moved {file} to {destination_directory}")
                log_success(file, destination_directory, timestamp)
            except (shutil.Error, IOError) as e:
                print(f"Failed to move {file}: {e}")
                log_error(file, e)
    # Return the timestamp
    return timestamp
  
def log_success(file, destination_directory, timestamp):
    log_dir = "logs"
    log_date = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    log_file = f"dtopy-{log_date}-moved.log"
    log_path = os.path.join(log_dir, log_file)

    success_message = f"{log_date}\t{file}\t{destination_directory}\n"

    with open(log_path, "a") as f:
        f.write(success_message)

def log_error(file, error):
    log_dir = "logs"
    log_date = datetime.datetime.now().strftime("%Y-%m-%d")
    log_file = f"dtopy-{log_date}-errors.log"
    log_path = os.path.join(log_dir, log_file)

    error_message = f"{datetime.datetime.now()}: Failed to move {file}. Error: {error}\n"

    with open(log_path, "a") as f:
        f.write(error_message)

def get_destination_directory(file_extension, base_directory):
    # Map file extensions to directories
    extension_directory_map = get_extension_directory_map()
    # Get the destination directory based on the file extension
    default_directory = get_default_directory()
    destination_directory = os.path.join(base_directory, extension_directory_map.get(file_extension, default_directory), file_extension.lstrip("."))

    return destination_directory
