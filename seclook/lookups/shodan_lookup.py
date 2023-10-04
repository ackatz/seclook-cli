import requests
from seclook.config_helper import load_config

base_url = "https://api.shodan.io/shodan/host/{}"


def search(value):
    config, shodan_api_key = load_config("shodan", key_required=False)
    headers = {"Accept": "application/json"}
    response = requests.get(
        base_url.format(value), headers=headers, params={"key": shodan_api_key}
    )
    return response.json()
