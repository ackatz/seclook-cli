import requests
import configparser
from seclook.find_config import find_config

config_path = find_config()
config = configparser.ConfigParser()
config.read(config_path)

base_url = "https://api.greynoise.io/v3/community/{}"


def search(value):
    greynoise_api_key = config["greynoise"]["api_key"]
    headers = {"Accept": "application/json", "key": greynoise_api_key}
    response = requests.get(base_url.format(value), headers=headers)
    return response.json()
