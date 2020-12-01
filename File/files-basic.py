# Описание задачи в файле Task.py
# cook_book = {
#   'Омлет': [
#     {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},
#     {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
#     {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
#     ],
#   'Утка по-пекински': [
#     {'ingredient_name': 'Утка', 'quantity': 1, 'measure': 'шт'},
#     {'ingredient_name': 'Вода', 'quantity': 2, 'measure': 'л'},
#     {'ingredient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'},
#     {'ingredient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'}
#     ],
#   'Запеченный картофель': [
#     {'ingredient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
#     {'ingredient_name': 'Чеснок', 'quantity': 3, 'measure': 'зубч'},
#     {'ingredient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'},
#     ]
#   }

from pprint import pprint

cook_book = dict()
key = ''
tmp_list = list()

with open('recipes.txt', 'r', encoding='utf-8') as f:
    for line in f:
        if not line.strip() == '' and not str(line.strip()).isdigit() and \
                '|' not in str(line.strip()):
            key = line.strip()

        if str(line.strip()).isdigit():
            continue
        if '|' in str(line.strip()):
            ingred = line.split('|')

            tmp_list.append(
                {
                    'ingredient_name': str(ingred[0]).strip(),
                    'quantity': int(str(ingred[1]).strip()),
                    'measure': str(ingred[2]).strip()
                }
            )

        if line.strip() == '':
            cook_book.setdefault(key, tmp_list)
            tmp_list.clear()

pprint(cook_book)
