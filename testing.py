
# GitHub Advanced Security - Push Protection Test

import requests

API_URL = "https://api.example.com"

# FAKE TEST SECRET - NOT A REAL CREDENTIAL
API_KEY = "ghp_1234567890abcdef1234567890abcdef1234"

headers = {
    "Authorization": f"Bearer {API_KEY}"
}

response = requests.get(API_URL, headers=headers)

print(response.status_code)
