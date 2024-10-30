import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '123'
HEADER = {'Content-Type' : 'application/json',
          'trainer_token': TOKEN }
def test_status_code(): 
    response = requests.get(url= f'{URL}/trainers', params = {'trainer_id': 8087})
    assert response.status_code == 200

def test_response():
    response = requests.get(url= f'{URL}/trainers', params = {'trainer_id': 8087})
    assert response.json()["data"][0]["trainer_name"] == 'Happypopka'

    