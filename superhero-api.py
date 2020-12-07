# Кто самый умный супергерой? Есть API по информации о супергероях. Нужно определить
# кто самый умный(intelligence) из трех супергероев- Hulk, Captain America, Thanos.
# Для определения id нужно использовать метод /search/name
#
# Токен, который нужно использовать для доступа к API: 2619421814940190.
# Таким образом, все адреса для доступа к API должны начинаться с https://superheroapi.com/api/2619421814940190/.
#
# ⚠️ Недавно сервис SuperHero API переехал на заблокированный Роскомнадзором IP-адрес, из-за чего
# некоторые интернет-провайдеры заблокировали к нему доступ, он может быть недоступен. В таком случае
# решайте это задание на REPL.it — оттуда всё должно быть доступно.


import requests


token = '2619421814940190'
heroes = ['Hulk', 'Captain America', 'Thanos']
url = f"https://superheroapi.com/api/{token}/search/"
max_intelligence = 0
max_heroes = ''

for hero in heroes:
    url_api = f"{url}/{hero}/"
    resp = requests.get(url_api)

    if resp.status_code != 200:
        raise Exception("всё очень плохо")

    intelligence = int(resp.json()['results'][0]['powerstats']['intelligence'])

    if intelligence > max_intelligence:
        max_intelligence = intelligence
        max_heroes = hero

print(f"Самый умный герой {max_heroes} с интеллектом {max_intelligence}!!!!")
