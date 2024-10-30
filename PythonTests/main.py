import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '123'
HEADER = {'Content-Type' : 'application/json',
          'trainer_token': TOKEN }
body_create = {
  "name": "DENISKAZAK",
  "photo_id": 1
}
body_put = {
    "pokemon_id": "119454",
    "name": "Hehehe",
    "photo_id": 1
}
body_post = {
    "pokemon_id": "119454"
}

response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)

response_put = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_put)
print(response_put.text)

response_post = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_post)
print(response_post.text)

response_getHappy = requests.get(url = f'{URL}/trainers',params = {'trainer_id' : 8087})
print(response_getHappy.text)