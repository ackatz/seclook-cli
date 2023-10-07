import configparser
from seclook.find_config import find_config
import textwrap
import sys


def load_config(service_name, key_required=True):
    try:
        config_path = find_config()
        config = configparser.ConfigParser()
        config.read(config_path)
    except configparser.ParsingError:
        print(
            textwrap.dedent(
                f"""
        ParsingError: Ensure the following lines are present in config.ini:

        [{service_name}]
        api_key = <Note: A key is{' required' if key_required
                else ' optional'} to use this API>
        """
            )
        )
        sys.exit()

    if key_required:
        try:
            api_key = config[service_name]["api_key"]
        except KeyError:
            print(
                textwrap.dedent(
                    f"""
            KeyError: Ensure the following lines are present in config.ini:

            [{service_name}]
            api_key = <Note: A key is required to use this API>
            """
                )
            )
            sys.exit()
    else:
        try:
            api_key = config[service_name].get("api_key", "")
        except KeyError:
            print(
                textwrap.dedent(
                    f"""
            KeyError: Ensure the following lines are present in config.ini:

            [{service_name}]
            api_key = <Note: A key is optional to use this API>
            """
                )
            )
            sys.exit()

    return config, api_key
