# Описание задачи в файле Task.py

from pprint import pprint


#из файла делается словарь
def file_in_dict(file):
    cook_book = dict()

    with open(file, 'r', encoding='utf-8') as f:
        tmp_list = list()
        key = ''
        for line in f:
            if not line.strip() == '' and not str(line.strip()).isdigit() and \
                    '|' not in str(line.strip()):
                key = line.strip()

            elif str(line.strip()).isdigit():
                num = int(line)
                i = 0

            elif '|' in str(line.strip()):
                i += 1
                ingred = str(line).strip().split('|')

                ingredient_name = str(ingred[0]).strip()
                quantity = int(str(ingred[1]).strip())
                measure = str(ingred[2]).strip()

                tmp_dict = dict(
                    ingredient_name = ingredient_name,
                    quantity = quantity,
                    measure = measure
                )

                tmp_list.append(tmp_dict)

                if i == num:
                    my_list = tmp_list[:]
                    cook_book[key] = my_list
                    del tmp_list[0:]

            elif line.strip() == '':
                continue

        return cook_book

#функция, которая на вход принимает список блюд из cook_book и количество персон для кого мы будем готовить
def get_shop_list_by_dishes(dishes, person_count):
   # breakpoint()
    shop_dict = dict()
    file = 'recipes.txt'
    recipes_dict = file_in_dict(file)
    ingred = ''

    for dish in dishes:
        if dish in recipes_dict:
            count_ingred = len(recipes_dict[dish])

            for i in range(count_ingred):
                ingred = recipes_dict[dish][i]['ingredient_name']

                if ingred not in shop_dict:
                    measure = recipes_dict[dish][i]['measure']
                    quantity = int(recipes_dict[dish][i]['quantity'])*person_count
                    shop_dict[ingred] = dict(
                        measure = measure,
                        quantity = quantity
                    )

                else:
                    tmp_quantity = int(shop_dict[ingred]['quantity'])
                    quantity = int(recipes_dict[dish][i]['quantity']) + tmp_quantity
                    shop_dict[ingred].update({'quantity': quantity})

        else:
            print(f'Блюда под названием {dish} нет среди наших рецептов! Подберите подходящее!')
            continue

    return shop_dict


#file = 'recipes.txt'
#cook_book = file_in_dict(file)
#pprint(cook_book)

get_shop = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет', 'Фахитос', 'Utka'], 3)
pprint(get_shop)

