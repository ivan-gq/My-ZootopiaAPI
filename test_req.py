# pip install requests
import requests

response = requests.get(
    "https://api.api-ninjas.com/v1/animals?name=srbin",
    headers={'X-Api-Key': 'cB7R0CSqMvAXDwL8q4BaVQYpjVEZvSQm100ker4x'},
    timeout=30,
)
response.raise_for_status()
print(response.json())