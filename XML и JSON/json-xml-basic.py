import json

with open('newsafr.json', encoding='utf-8') as f:
    json_data = json.load(f)

list_words = list()
set_words = set()
tmp_str = ''


len_json = len(json_data["rss"]["channel"]["items"])

#создание большой строки со всеми данными из дескрипшен
for i in range(len_json):
    my_words = (json_data["rss"]["channel"]["items"][i]["description"]).lower()
    tmp_str += ''.join(my_words)

#список с уникальными словами
list_words = list(tmp_str.split())
poisk = dict()

for elem in list_words:
    len_word = len(elem)

    if len_word > 6:

        #print(elem)
        if elem in poisk:
            poisk[elem] += 1
        else:
            poisk[elem] = 1
print(poisk)
#сортировка словаря: выходе получается список из кортежей
list_d = list(poisk.items())
list_d.sort(key=lambda i: i[1])

#печать первых 10 слов
for el in list_d[0:10]:
    print(el)