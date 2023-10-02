import requests
import configparser
from seclook.find_config import find_config

config_path = find_config()
config = configparser.ConfigParser()
config.read(config_path)

shodan_api_key = config["shodan"]["api_key"]

base_url = "https://api.shodan.io/shodan/host/{}"


def search(value):
    headers = {"Accept": "application/json"}
    response = requests.get(
        base_url.format(value), headers=headers, params={"key": shodan_api_key}
    )
    return response.json()
