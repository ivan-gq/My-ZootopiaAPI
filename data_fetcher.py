import requests
import os

API_KEY = "cB7R0CSqMvAXDwL8q4BaVQYpjVEZvSQm100ker4x"
API_URL = "https://api.api-ninjas.com/v1/animals"

def fetch_data(animal_name):
    """Fetches animal data from the API."""
    response = requests.get(
        f"{API_URL}?name={animal_name}",
        headers={'X-Api-Key': API_KEY},
        timeout=30,
        )
    response.raise_for_status()
    animals_data = response.json()
    return animals_data