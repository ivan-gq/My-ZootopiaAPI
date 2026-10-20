import json

HTML_FILE = "animals.html"
JSON_FILE = "animals_data.json"


def load_data(file_path):
    """Loads a JSON file securely with UTF-8 encoding."""
    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def get_skin_types(data):
    """Returns a set of all available, lowercased skin types."""
    # Using a set comprehension is faster and more Pythonic
    return {
        animal.get('characteristics', {}).get('skin_type').lower()
        for animal in data
        if animal.get('characteristics', {}).get('skin_type')
    }


def serialize_animal(data):
    """Generate serialized HTML tags per animal."""
    # Use .get() chained safely to avoid KeyError on missing fields
    name = data.get('name', 'Unknown Animal')
    chars = data.get('characteristics', {})
    diet = chars.get('diet', 'Unknown')
    
    # ".join()" handles formatting perfectly without trailing commas
    locations_str = ", ".join(data.get('locations', []))
    
    # Build list items dynamically
    li_tags = [
        f"<li><strong>Diet:</strong> {diet}</li>",
        f"<li><strong>Location:</strong> {locations_str}</li>"
    ]
    
    animal_type = chars.get('type')
    if animal_type:
        li_tags.append(f"<li><strong>Type:</strong> {animal_type}</li>")
        
    skin_type = chars.get('skin_type')
    if skin_type:
        li_tags.append(f"<li><strong>Skin type:</strong> {skin_type}</li>")
        
    # Join the tags together for the final f-string injection
    li_html = "\n\t\t\t".join(li_tags)
    
    # Multi-line f-strings are much faster than += concatenation
    return f"""<li class="cards__item">
\t<div class="card__title"> {name}</div>
\t<div class="card__text">
\t\t<ul>
\t\t\t{li_html}
\t\t</ul>
\t</div>
</li>\n"""


def main():
    """Main function."""
    animals_data = load_data(JSON_FILE)

    with open("animals_template.html", "r", encoding="utf-8") as file:
        html_content = file.read()

    # Collect HTML chunks in a list (much faster than concatenating strings in a loop)
    output_list = []
    
    while True:
        user_choice = input("Filter by skin type [yes/no]: ").strip().lower()
        
        if user_choice in ("yes", "y"):
            skin_types = get_skin_types(animals_data)
            print("Available skin types: ")
            
            # Print available types on one line dynamically
            print("\t" + " ".join(skin.title() for skin in skin_types))

            while True:
                display_skin_type = input("\nEnter skin type from selection above: ").strip().lower()
                
                if display_skin_type in skin_types:
                    # Filter and serialize in one efficient list comprehension
                    output_list = [
                        serialize_animal(animal) for animal in animals_data
                        if animal.get('characteristics', {}).get('skin_type', '').lower() == display_skin_type
                    ]
                    break
                else:
                    print("Skin type not available :(")
            break

        elif user_choice in ("no", "n"):
            print("no")
            output_list = [serialize_animal(animal) for animal in animals_data]
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

    # Join the accumulated HTML blocks all at once
    new_page = html_content.replace("__REPLACE_ANIMALS_INFO__", "".join(output_list))
    
    with open(HTML_FILE, "w", encoding="utf-8") as file:
        file.write(new_page) # .write() returns character count, no need to assign it to a variable
        
    print(f"HTML file {HTML_FILE} updated.")


if __name__ == "__main__":
    main()