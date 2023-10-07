import os


def find_config():
    dirs_to_check = [
        os.getcwd(),
        os.path.dirname(os.path.abspath(__file__)),
        os.path.join(os.path.expanduser("~"), ".seclook"),
    ]

    for directory in dirs_to_check:
        config_path = os.path.join(directory, "config.ini")
        if os.path.exists(config_path):
            return config_path

    raise FileNotFoundError(
        "No config.ini file found in any of the checked directories:\n"
        "({})".format(", ".join(dirs_to_check)) + "\n"
        "Copy and rename config.ini.sample as config.ini into "
        "any of the directories mentioned above:\n"
        "https://github.com/ackatz/seclook/blob/main/config.ini.sample"
    )
