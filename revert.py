import os
import shutil
import datetime
import argparse
import json

# python revert.py path/to/logfile.log

def revert_files(log_file):
    with open(log_file, "r") as f:
        lines = f.readlines()

    destination_parent_dir = ""

    for line in lines:
        fields = line.strip().split("\t")
        if len(fields) == 3:
            timestamp, file, destination_path = fields
            source_path = os.path.join(destination_path, file)
            destination_parent_dir = os.path.dirname(os.path.dirname(destination_path))

            if os.path.exists(source_path):
                try:
                    shutil.move(source_path, os.path.join(destination_parent_dir, file))
                    print(f"Moved {file} back to {os.path.join(destination_parent_dir, file)}")
                    log_success_revert(file, source_path, destination_path)
                except (shutil.Error, IOError) as e:
                    print(f"Failed to move {file} back: {e}")
                    log_error_revert(file, source_path, destination_path)
            else:
                print(f"Original file {file} not found at {source_path}")
                log_error_revert(file, source_path, destination_path)
                

    delete_empty_directories(destination_parent_dir)
    
    
def log_success_revert(file, source_path, destination_path):
    log_dir = "logs"
    log_date = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    log_file = f"dtopy-{log_date}-reverted.log"
    log_path = os.path.join(log_dir, log_file)

    success_message = f"{log_date}\t{file}\t{source_path}\t{destination_path}\n"

    with open(log_path, "a") as f:
        f.write(success_message)

def log_error_revert(file, source_path, destination_path):
    log_dir = "logs"
    log_date = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    log_file = f"dtopy-{log_date}-revert-errors.log"
    log_path = os.path.join(log_dir, log_file)

    error_message = f"{log_date}\t{file}\t{source_path}\t{destination_path}\n"

    with open(log_path, "a") as f:
        f.write(error_message)

def delete_empty_directories(destination_parent_dir):
    config_data = load_config()
    extension_directory_map = config_data.get('extension_directory_map', {})
    default_directory = config_data.get('defaults', {}).get('default_directory', 'Other')
    print(f"Deleting empty directories in {destination_parent_dir}")

    for ext in extension_directory_map:
        directory = extension_directory_map[ext]
        directory_path = os.path.join(destination_parent_dir, directory, ext.lstrip("."))
        print(f"Checking directory: {directory_path}")
        if not os.path.exists(directory_path):
            continue

        if not os.path.isdir(directory_path):
            continue

        if not os.listdir(directory_path):
            shutil.rmtree(directory_path)
            print(f"Deleted empty directory: {directory_path}")

def load_config():
    with open('config.json', 'r') as f:
        config_data = json.load(f)
    return config_data

def main():
    parser = argparse.ArgumentParser(description="Revert files to their original locations based on a log file.")
    parser.add_argument("log_file", help="Path to the log file")
    args = parser.parse_args()

    if os.path.isfile(args.log_file):
        revert_files(args.log_file)
    else:
        print("Invalid log file path.")

if __name__ == "__main__":
    main()
