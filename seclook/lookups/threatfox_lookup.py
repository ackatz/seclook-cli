import requests
import configparser
from seclook.find_config import find_config

config_path = find_config()
config = configparser.ConfigParser()
config.read(config_path)

base_url = "https://threatfox-api.abuse.ch/api/v1/"


def search(value):
    headers = {
        "Content-Type": "application/json",
        "API-KEY": config["threatfox"]["api_key"],
    }
    payload = {"query": "search_ioc", "search_term": value}
    response = requests.post(base_url, headers=headers, json=payload)
    return response.json()
