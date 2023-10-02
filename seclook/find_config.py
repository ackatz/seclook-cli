import os


def find_config():
    # List of directories to look in
    dirs_to_check = [
        os.getcwd(),  # Current working directory
        os.path.dirname(os.path.abspath(__file__)),  # Directory of this script
        os.path.join(
            os.path.expanduser("~"), ".seclook"
        ),  # A .seclook directory in the user's home directory
    ]

    for dir in dirs_to_check:
        config_path = os.path.join(dir, "config.ini")
        if os.path.exists(config_path):
            return config_path

    raise FileNotFoundError(
        "No config.ini file found in any of the checked directories"
    )
