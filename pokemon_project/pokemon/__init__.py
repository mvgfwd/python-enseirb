#!/usr/bin/env python3
import sys
import requests
import json
import platformdirs
import os.path

"""
Pokemon exercise
"""

__version__ = "0.0.1"


CACHE_DIR = platformdirs.user_cache_dir('pokemon')

class Pokemon:
    def __init__(self, id, name, height, weight, types, stats, moves, sprite_url, **kwargs):
        self.id = id
        self.name = name
        self.height = height
        self.weight = weight
        self.types = types
        self.stats = stats
        self.moves = moves
        self.sprite_url = sprite_url

    @classmethod
    def get(cls, id_or_name):
        data = cls.fetch(cls, id_or_name)
        LEGENDARY_API_URL = 'https://pokeapi.co/api/v2/pokemon-species/'
        legend_api = requests.get(f"{LEGENDARY_API_URL}{id_or_name}")
        legend_data = legend_api.content
        legend_load = json.loads(legend_data)
        is_legendary = legend_load['is_legendary']
        new_poke = LegendaryPokemon(**data) if is_legendary else Pokemon(**data)
        return new_poke

    def fetch(self, pokemon_name):
        if self.retrieve_cache(pokemon_name):
            data = self.retrieve_cache(pokemon_name)
            print("FROM CACHE")
        else:
            POKE_API_URL = 'https://pokeapi.co/api/v2/pokemon/'
            poke_api = requests.get(f"{POKE_API_URL}{pokemon_name}")
            poke_data = poke_api.content
            data = json.loads(poke_data)
            self.cache_res(data, pokemon_name)
            print("NEW CACHE")
        #the data
        res = {
            "id" : data['id'],
            "name" : data['forms'][0]['name'],
            "height" : data['height'] ,
            "weight" : data['weight'] ,
            "types" : [[x['type']['name'] for x in data['types']]][0],
            "stats" : {x['stat']['name']: x['base_stat'] for x in data['stats']},
            "moves" : [x['move']['name'] for x in data['moves']],
            "sprite_url" : data['sprites']['front_default']
        }
        return res
    
    def cache_res(json_data, po_name):
        os.path.join(platformdirs.user_cache_dir('pokemon'))
        os.makedirs(CACHE_DIR, exist_ok=True)
        f = open(f'{CACHE_DIR}/{po_name.lower()}.json', 'w')
        f.write(json.dumps(json_data))
        f.close()

    def retrieve_cache(poke):
        try: #take from cache
            with open(f'{CACHE_DIR}/{poke.lower()}.json', 'r') as f:
                return json.load(f)
        except: #create the cache
            return False

    def print_info(self):
        print(f"Ordinary Poke: {self.name.capitalize()}")
        for k, v in self.stats.items():
            print(f"{k}: {v}")


class LegendaryPokemon(Pokemon):
        
    def print_info(self):
        print(f"⭐Legendary Poke: {self.name.capitalize()}")
        for k, v in self.stats.items():
            print(f"{k}: {v}")


if __name__ == '__main__':
    if len(sys.argv) > 1 :
        p = Pokemon.get(sys.argv[1])
        p.print_info()
    else:
        print("Please provide a pokemon name")

