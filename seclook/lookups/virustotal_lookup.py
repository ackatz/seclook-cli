import requests
from seclook.config_helper import load_config

base_url = "https://www.virustotal.com/api/v3/search"


def search(value):
    config, virustotal_api_key = load_config("virustotal")
    headers = {"x-apikey": virustotal_api_key}
    params = {"query": value}
    response = requests.get(base_url, headers=headers, params=params)
    return response.json()
