# Animal Info Fetcher

A simple Python script that queries the API Ninjas Animals API to retrieve facts about a specific animal and generates a formatted HTML file displaying its characteristics.

## Features

- **Dynamic Data Retrieval:** Prompts the user for an animal name and fetches real-time data using a custom `data_fetcher` module.
- **HTML Generation:** Parses the JSON response (Diet, Location, Type, Skin Type) and injects the data into an HTML template (`animals_template.html`).
- **Error Handling:** Gracefully handles non-existent animals by generating an appropriate message in the HTML output.

## Prerequisites

- Python 3.x
- `animals_template.html` (Must be in the same directory, containing the `__REPLACE_ANIMALS_INFO__` placeholder)
- An active API key from [API Ninjas](https://api-ninjas.com/) (Configured in your `data_fetcher.py` file)

## Usage

1. Clone the repository and navigate to the project folder.
2. Run the script:
   ```bash
   python main.py
   ```
3. Enter the name of the animal you want to look up when prompted.
4. Open the newly generated `animals.html` file in your web browser to view the generated animal cards.