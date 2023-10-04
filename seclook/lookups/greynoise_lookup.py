import requests
from seclook.config_helper import load_config

base_url = "https://api.greynoise.io/v3/community/{}"


def search(value):
    config, greynoise_api_key = load_config("greynoise", key_required=False)
    headers = {"Accept": "application/json", "key": greynoise_api_key}
    response = requests.get(base_url.format(value), headers=headers)
    return response.json()
