import requests
from seclook.config_helper import load_config

base_url = "https://emailrep.io/{}"


def search(value):
    config, emailrep_api_key = load_config("emailrep")
    headers = {"Key": emailrep_api_key}
    response = requests.get(base_url.format(value), headers=headers)
    return response.json()
