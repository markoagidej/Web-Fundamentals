# Task 1: Setting Up a Python Virtual Environment and Installing Packages
import requests
import json

# Task 2: Fetching Data from the Pokémon API
response = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu")
json_data = response.text
poke_data = json.loads(json_data)

print(f"Name: {poke_data["name"]}")
print(f"Abilities:")
for ability in poke_data["abilities"]:
    print(ability["ability"]["name"])

# Task 3
def fetch_pokemon_data(pokemon_name):
    # response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}")
    # json_data = response.text
    # poke_data = json.loads(json_data)
    return json.loads(requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}").text)

def calculate_average_weight(pokemon_list):
    total_weight = 0
    for pokemon in pokemon_list:
        poke_data = fetch_pokemon_data(pokemon)
        total_weight += poke_data["weight"]
        print(f"Name: {poke_data["name"]}")
        print(f"Abilities:")
        for ability in poke_data["abilities"]:
            print(ability["ability"]["name"])
    return total_weight / len(pokemon_list)

pokemon_names = ["pikachu", "bulbasaur", "charmander"]

avg_weight = calculate_average_weight(pokemon_names)
print(f"Average weight = {avg_weight}")