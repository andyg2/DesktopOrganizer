import os
import argparse
from organizer import organize_files

def main():
    parser = argparse.ArgumentParser(description="Organize files in a directory.")
    parser.add_argument("base_directory", nargs="?", default=None, help="Path to the base directory")
    args = parser.parse_args()
      
    
    print("Organizing files...")

    base_directory = args.base_directory or get_default_base_directory()

    if os.path.isdir(base_directory):
        script_path = os.path.dirname(os.path.realpath(__file__))
        timestamp = organize_files(base_directory)
        logs_directory = os.path.join(script_path, 'logs')
        os.makedirs(logs_directory, exist_ok=True)

        # Construct the revert command text
        log_file = os.path.abspath(os.path.join(logs_directory, f'dtopy-{timestamp}-moved.log'))
        print(log_file);
        if os.path.isfile(log_file):
            revert_command = f"python revert.py {log_file}"
            print("Organized files successfully. Run the following command to revert the changes:")
            print(revert_command)

            # Append the revert command to the revert history log file
            revert_history_file = os.path.join(logs_directory, 'revert_history.txt')
            with open(revert_history_file, 'a') as f:
                f.write(revert_command + '\n')    
                
        else:
            print(f"No files were moved.")
    else:
        print("Invalid base directory path.")


def get_default_base_directory():
    config_data = load_config()
    default_base_directory = config_data.get('defaults', {}).get('default_base_directory')
    if default_base_directory and os.path.isdir(default_base_directory):
        return default_base_directory
    else:
        return os.path.join(os.path.expanduser("~"), "Desktop")

if __name__ == "__main__":
    main()
