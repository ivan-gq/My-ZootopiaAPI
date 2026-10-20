import requests
from dotenv import load_dotenv
import os

# 1. Load the key without a fallback
load_dotenv()
API_KEY = os.getenv("API_KEY")

# 2. Force the script to crash safely if the key is missing
if not API_KEY:
    raise ValueError("API_KEY environment variable is missing!")

API_URL = "https://api.api-ninjas.com/v1/animals"

def fetch_data(animal_name):
    """Fetches animal data from the API."""
    try:
        response = requests.get(f"{API_URL}?name={animal_name}", headers={'X-Api-Key': API_KEY}, timeout=30,)
        response.raise_for_status()
        animals_data = response.json()
        if not animals_data:
            return []
        else:
            return animals_data
    except requests.RequestException as e:
        print(f"Error fetching data for {animal_name}: {e}")
        return []