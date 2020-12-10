# Самый важный сайт для программистов это stackoverflow. И у него тоже есть API Нужно написать программу, которая выводит
# все вопросы за последние два дня и содержит тэг 'Python'. Для этого задания токен не требуется.

import requests


resp = requests.get(
    'https://api.stackexchange.com/2.2/questions?',
    params={
        'fromdate': '2020-12-09',
        'todate': '2020-12-10',
        'order': 'desc',
        'tagged': 'python',
        'site': 'stackoverflow',
        'pagesize': '100',
    }
)

data = resp.json()
all_items = len(data['items'])

for i in range(all_items):
    print(data['items'][i]['title'])
