#Sharon Lurye
#6/16/21
#Homework 3, Part 1

import requests

response = requests.get("https://pokeapi.co/api/v2/pokemon/55")

data = response.json()

print(data.keys())

#What is the URL to the documentation?
#Answer: https://pokeapi.co/docs/v2

# What pokemon has the ID of 55?
print(data['name']) 

#Golduck

# How tall is that pokemon?

print(data['height'])

#17 decimeters 

# How many versions of Pokemon games have been released?

#Can't be answered by API 

#https://pokeapi.co/api/v2/version -- "Count" is 34
#https://pokeapi.co/api/v2/version?limit=34

# Print out the name of every electric-type pokemon.

response = requests.get("https://pokeapi.co/api/v2/type/electric")

electric_type = response.json()

#print(electric_type['pokemon'][0]['pokemon']['name'])

for pokemon in electric_type['pokemon']:
    print(pokemon['pokemon']['name'])

# What are electric-type Pokemon called in the Korean version of the game?

print(electric_type['names'][1]['name'])

for lang in electric_type['names']:
    if lang['language']['name'] == 'ko':
        print(lang['name'])

#They are called 전기 (Jeongi)

# Who has a higher speed stat, Eevee or Pikachu?

eevee = (requests.get("https://pokeapi.co/api/v2/pokemon/eevee")).json()
pikachu = (requests.get("https://pokeapi.co/api/v2/pokemon/pikachu")).json()

print("Eevee's speed is", eevee['stats'][-1]['base_stat'])
print("Pikachu's speed is", pikachu['stats'][-1]['base_stat'])

#Pikachu is faster