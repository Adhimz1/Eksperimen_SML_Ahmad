import requests
import sys

token = "8364586877:AAFHG3SlYW83XHU8QVP9P_0LB88SHYYrT9o"
chat_id = "8827548319"
url = f"https://api.telegram.org/bot{token}/sendMessage"

data = {
    "chat_id": chat_id,
    "text": "Hello from testing script!"
}

response = requests.post(url, json=data)
print(f"Status Code: {response.status_code}")
print(f"Response: {response.text}")
