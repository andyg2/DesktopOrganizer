import json

def load_config():
    with open('config.json', 'r') as f:
        config_data = json.load(f)
    return config_data

def get_extension_directory_map():
    config_data = load_config()
    extension_directory_map = config_data.get('extension_directory_map', {})
    return extension_directory_map

def get_default_directory():
    config_data = load_config()
    default_directory = config_data.get('defaults', {}).get('default_directory', 'Other')
    return default_directory
