import requests
import configparser
from seclook.find_config import find_config

config_path = find_config()
config = configparser.ConfigParser()
config.read(config_path)

base_url = "https://api.abuseipdb.com/api/v2/check"


def search(value):
    abuseipdb_api_key = config["abuseipdb"]["api_key"]
    headers = {"Accept": "application/json", "Key": abuseipdb_api_key}
    params = {"ipAddress": value, "maxAgeInDays": 90, "verbose": True}
    response = requests.get(base_url, headers=headers, params=params)
    return response.json()
