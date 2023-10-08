import requests
from seclook.config_helper import load_config

base_url = "https://api.openai.com/v1/chat/completions"


def search(service, json_response):
    config, openai_api_key = load_config("openai")
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + openai_api_key,
    }
    payload = {
        "model": "gpt-4",
        "messages": [
            {
                "role": "user",
                "content": f"You are a security analyst summarizer. "
                f"Given the following JSON response from {service}"
                f", summarize the response to tell me what I need to know: "
                f"{json_response}",
            }
        ],
    }
    response = requests.post(base_url, headers=headers, json=payload)
    return response.json()
