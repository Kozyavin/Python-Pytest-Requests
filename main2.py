"""
Kolorado test API
"""
import requests

URL = 'https://api.pokemonbattle.me:9104'
HEADER = {'Content-Type': 'application/json',
          'trainer_token': '7f56b985aa880bf2f7fc7f6f65e91157'}

# СОЗДАНИЕ ПОКЕМОНА (get)

body_newPok = {
      "name": "generate",
      "photo": "generate"
 }
response = requests.post(url = f'{URL}/pokemons', json = body_newPok, headers = HEADER)
print(f'Статус код:{response.status_code}. {response.json()["message"]}')

#заводим переменную с ID созданного покемона
new_pokemonID = response.json()["id"] 

# СМЕНА ИМЕНИ ПОКЕМОНА (patch)

body_chengeName = {
      "pokemon_id": new_pokemonID,
      "name": "New Name"
 }
response = requests.patch(url = f'{URL}/pokemons', json = body_chengeName, headers = HEADER)
print(f'Статус код:{response.status_code}. {response.json()["message"]}')


# ПОЙМАТЬ ПОКЕМОНА В ПОКЕБОЛ (post)

body_catchPokemon = {
      "pokemon_id": new_pokemonID
}
response = requests.post(url = f'{URL}/trainers/add_pokeball', json = body_catchPokemon, headers = HEADER)
print(f'Статус код:{response.status_code}. {response.json()["message"]}')