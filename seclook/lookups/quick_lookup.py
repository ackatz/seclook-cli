import requests

base_url = "https://quick.akatz.org/api/v1/check"

def search(value):
    headers = {"Accept": "application/json"}
    response = requests.get(
        base_url.format(value),
        headers=headers,
        params={"ipAddress": value},
    )
    return response.json()
