import requests
from seclook.config_helper import load_config

base_url = "https://threatfox-api.abuse.ch/api/v1/"


def search(value):
    config, threatfox_api_key = load_config("threatfox", key_required=False)
    headers = {
        "Content-Type": "application/json",
        "API-KEY": threatfox_api_key,
    }
    payload = {"query": "search_ioc", "search_term": value}
    response = requests.post(base_url, headers=headers, json=payload)
    return response.json()
