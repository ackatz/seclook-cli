import requests
import configparser
from seclook.find_config import find_config

config_path = find_config()
config = configparser.ConfigParser()
config.read(config_path)

virustotal_api_key = config["virustotal"]["api_key"]

base_url = "https://www.virustotal.com/api/v3/search"


def search(value):
    headers = {"x-apikey": virustotal_api_key}
    params = {"query": value}
    response = requests.get(base_url, headers=headers, params=params)
    return response.json()
