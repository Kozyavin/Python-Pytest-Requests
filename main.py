"""
Kolorado test API
"""
# РЕГИСТРАЦИЯ НОВОГО ТРЕНЕРА (post)
import requests

URL = 'https://api.pokemonbattle.me:9104'
HEADER = {'Content-Type': 'application/json'}

# body = {
#     "trainer_token": "7f56b985aa880bf2f7fc7f6f65e91157",
#     "email": "kozyavin.volodimir@yandex.ru",
#     "password": "Fantango86!"
# }

# response = requests.post(url = f'{URL}/trainers/reg', json = body, headers = HEADER, timeout = 5)
# print(f'Статус код:{response.status_code}. Сообщение: {response.json()["message"]}')


# ПОЛУЧЕНИЕ СПИСКА ТРЕНЕРОВ (get)

response = requests.get(url = f'{URL}/trainers', params = {'level': 1, 'page': 0}, timeout= 3)
#print(f'Статус код:{response.status_code}.  Сообщение: {response.json()}')

print(f'Статус код:{response.status_code}')

json_data = response.json()

# Если кол-во тренеров >= 61 , то ОК
if len(json_data) >= 61:
    print('Ok')
else:
    print('Bad')