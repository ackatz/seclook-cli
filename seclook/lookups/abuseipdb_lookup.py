import requests
from seclook.config_helper import load_config

base_url = "https://api.abuseipdb.com/api/v2/check"


def search(value):
    config, abuseipdb_api_key = load_config("abuseipdb")
    headers = {"Accept": "application/json", "Key": abuseipdb_api_key}
    params = {"ipAddress": value, "maxAgeInDays": 90, "verbose": True}
    response = requests.get(base_url, headers=headers, params=params)
    return response.json()
