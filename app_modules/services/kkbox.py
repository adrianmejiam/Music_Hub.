# KKBOX API Example
import requests

url = "https://developer.kkbox.com"
headers = {
    "Content-Type": "application/json"
}

response = requests.get(url)
data = response.json()
print(data)
