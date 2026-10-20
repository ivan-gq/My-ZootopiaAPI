import json

HTML_FILE = "animals.html"
JSON_FILE = "animals_data.json"

def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)


def get_skin_types(data):
    skin_types = set()
    for animal in data:
        skin = animal['characteristics'].get('skin_type')
        if skin:
            skin_types.add(skin.lower())

    return skin_types


def serialize_animal(data):
    '''Generate serialized HTML tags per animal
    '''
    output_str = ''
    output_str += '<li class="cards__item">\n'
    output_str += f'\t<div class="card__title"> {data['name']}</div>\n'
    output_str += '\t<div class="card__text">\n'
    output_str += '\t\t<ul>\n'
    output_str += f"\t\t\t<li><strong>Diet:</strong> {data['characteristics']['diet']}</li>\n"
    output_str += f"\t\t\t<li><strong>Location: </strong>"
    for i in range(len(data['locations'])):
        output_str += f"{data['locations'][i]}"
        if len(data['locations']) > 1:
            output_str += ", "
    output_str += "</li>\n"
    animal_type = data['characteristics'].get('type')
    skin_type = data['characteristics'].get('skin_type')
    if animal_type:
        output_str += f"\t\t\t<li><strong>Type: </strong>{animal_type}</li>\n"
    if skin_type:
        output_str += f"\t\t\t<li><strong>Skin type: </strong>{skin_type}</li>\n"
    output_str += "\t\t</ul>\n\t</div>\n</li>\n"
    return output_str


def main():
    '''Main fucntion'''
    animals_data = load_data(JSON_FILE)

    with open("animals_template.html", "r", encoding="utf-8") as file:
        html_content = file.read()

    output_str = ''
    while True:
        user_choice = input("Filter by skin type [yes/no]:").strip()
        if user_choice.lower() == "yes" or user_choice.lower() == "y":
            skin_types = get_skin_types(animals_data)
            print("Available skin types: ")
            for skin in skin_types:
                print(f"\t{skin.title()}", end=" ")

            while True:
                user_choice = input("\nEnter skin type from selection above:").strip()
                if user_choice.lower() in skin_types:
                    display_skin_type = user_choice.lower()
                    for animal in animals_data:
                        if animal['characteristics'].get('skin_type').lower() == display_skin_type:
                            output_str += serialize_animal(animal)
                    break   #break skin input while loop
                else:
                    print("Skin type not available :(")
            break   #break main while loop

        elif user_choice.lower() == "no" or user_choice.lower() == "n":
            print("no")
            for animal in animals_data:
                output_str += serialize_animal(animal)
            break

    new_page = html_content.replace("__REPLACE_ANIMALS_INFO__", output_str)
    

    with open(HTML_FILE, "w", encoding="utf-8") as file:
        html_content = file.write(new_page)
    print(f"HTML file {HTML_FILE} updated.")


if __name__ == "__main__":
    main()
