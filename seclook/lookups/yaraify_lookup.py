import requests

base_url = "https://yaraify-api.abuse.ch/api/v1/"


def search(value):
    data = {"query": "lookup_hash", "search_term": f"{value}"}
    headers = {"Content-Type": "application/json"}
    response = requests.post(base_url, headers=headers, json=data)
    return response.json()
