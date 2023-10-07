import requests
from seclook.config_helper import load_config

base_url = "https://pulsedive.com/api/info.php"


def search(value):
    config, pulsedive_api_key = load_config("pulsedive", key_required=False)
    headers = {"Accept": "application/json"}
    response = requests.get(
        base_url.format(value),
        headers=headers,
        params={"key": pulsedive_api_key, "indicator": value},
    )
    return response.json()
