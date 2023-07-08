# DesktopTidy

A simple files organizer in Python to move files into subdirectories based on their types.

## Author

- [@andyg2](https://www.github.com/andyg2)

## Installation

`git clone https://github.com/andyg2/DesktopOrganizer.git`
`cd DesktopOrganizer`

## Documentation

`python main.py /messy/directory`

Every file in that directory will be moved into a subdirectory based on the file type (configurable in config.json).
Subdirectories are unaffected.

### For example

`/messy/directory/image.jpg` will be moved to `/messy/directory/Images/jpg/image.jpg`

`/messy/directory/data.csv` will be moved to `/messy/directory/Documents/csv/data.csv`

Unmatched file types will be moved to the `Other` directory.

## Logging and reverting changes

All file movements are logged to the console and to a log file. The log file can also be parsed to revert those changes by executing a vevert command, which is also shown in the console

```console
Moved data.csv to /messy/directory/Documents/csv
Moved Dropbox.zip to /messy/directory/Archives/zip
Moved abc.url to /messy/directory/Other/url

Organized files successfully. Run the following command to revert the changes:
python revert.py /script/path/logs/dtopy-2023-06-05-05-02-50-moved.log
```

## Configuration

config.json - update to suit your needs

```json
{
  "extension_directory_map": {
    ".jpg": "Images",
    ".png": "Images",
    ".bmp": "Images",
    ".gif": "Images",
    ".mp3": "Music",
    ".wav": "Music",
    ".flac": "Music",
    ".mp4": "Videos",
    ".avi": "Videos",
    ".mkv": "Videos",
    ".docx": "Documents",
    ".xlsx": "Documents",
    ".pptx": "Documents",
    ".txt": "Documents",
    ".pdf": "Documents",
    ".csv": "Documents",
    ".html": "Documents",
    ".py": "Documents",
    ".java": "Documents",
    ".cpp": "Documents",
    ".ppt": "Documents",
    ".xls": "Documents",
    ".doc": "Documents",
    ".psd": "Documents",
    ".ai": "Documents",
    ".svg": "Documents",
    ".zip": "Archives",
    ".rar": "Archives",
    ".7z": "Archives",
    ".exe": "Programs",
    ".msi": "Programs"
  },
  "defaults": {
    "default_directory": "Other"
  }
}
```

## Notes

The repo consists of the following files and basic structure

### config.py

- import json

### main.py

- import os
- import argparse
- from organizer import organize_files

### organizer.py

- import os
- import shutil
- import datetime
- from config import get_extension_directory_map, get_default_directory

### revert.py

- import os
- import shutil
- import datetime
- import argparse
- import json

## Badges

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
