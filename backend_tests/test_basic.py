import requests
import pytest

URL = 'https://api.pokemonbattle.me:9104'
HEADER = {'Content-Type':'application/json'}

def test_get_trainers():
    
    # Get trainers by level = 5

    response = requests.get(url=f'{URL}/trainers', params={'level':5}, timeout=5)
    assert response.status_code == 200, 'Unexpected status code'

def test_get_trainers_name_city_code():

    # Get my trainer with name and city + code response
    
    response = requests.get(url=f'{URL}/trainers', params={'trainer_id':3552}, timeout=5)
    assert response.status_code == 200, 'Unexpected status code'
    assert response.json()['city'] == 'Брянск',''
    assert response.json()['trainer_name'] == 'KIOCI',''