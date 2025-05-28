#!/usr/bin/env python3
import sys
import requests
import json

"""
Pokemon exercise
"""

__version__ = "0.0.1"


class Pokemon:
    def __init__(self, pokemon_name):
        poke_data = self.fetch(pokemon_name)
        self._set_data(**poke_data)

    def _set_data(self, id, name, height, weight, types, stats, moves, sprite_url, **kwargs):
        self.id = id
        self.name = name
        self.height = height
        self.weight = weight
        self.types = types
        self.stats = stats
        self.moves = moves
        self.sprite_url = sprite_url

    def fetch(self, pokemon_name):
        POKE_API_URL = 'https://pokeapi.co/api/v2/pokemon/'
        poke_api = requests.get(f"{POKE_API_URL}{pokemon_name}")
        poke_data = poke_api.content
        data = json.loads(poke_data)
        #the data
        res = {
            "id" : data['id'],
            "name" : data['forms'][0]['name'],
            "height" : data['height'] ,
            "weight" : data['weight'] ,
            "types" : [[x['type']['name'] for x in data['types']]][0],
            "stats" : {x['stat']['name']: x['base_stat'] for x in data['stats']}, #FIXME
            "moves" : [x['move']['name'] for x in data['moves']], #FIXME
            "sprite_url" : data['sprites']['front_default']
        }
        return res

    def print_info(self):
        print(f"Name: {self.name.capitalize()}")
        for k, v in self.stats.items():
            print(f"{k}: {v}")


class LegendaryPokemon(Pokemon):
        
    def print_info(self):
        print(f"Legendary Poke: {self.name.capitalize()}")



# bulbasaur = LegendaryPokemon(
#     id=1,
#     name="bulbasaur",
#     height=7,           # decimetres (0.7m)
#     weight=69,          # hectograms (6.9kg)
#     types=["grass", "poison"],
#     stats={
#         "hp": 45,
#         "attack": 49,
#         "defense": 49,
#         "special-attack": 65,
#         "special-defense": 65,
#         "speed": 45
#     },
#     moves=["tackle", "growl", "leech-seed", "vine-whip"],
#     sprite_url="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/1.png"
# )


#building package
# python -m flit init


if __name__ == '__main__':
    if len(sys.argv) > 1 :
        Pokemon(sys.argv[1])
    else:
        print("Please provide a pokemon name")
