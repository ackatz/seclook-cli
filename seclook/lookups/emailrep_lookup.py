import requests
import configparser
from seclook.find_config import find_config

config_path = find_config()
config = configparser.ConfigParser()
config.read(config_path)

emailrep_api_key = config["emailrep"]["api_key"]

base_url = "https://emailrep.io/{}"


def search(value):
    headers = {"Key": emailrep_api_key}
    response = requests.get(base_url.format(value), headers=headers)
    return response.json()
