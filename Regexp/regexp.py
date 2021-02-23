from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv
import re
from itertools import chain

with open("phonebook_raw.csv", encoding='UTF-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

# pprint(str(contacts_list[1][0]).split(' '))
# pprint(contacts_list)


new_list = list()
tmp_list = list()
contacts_list_new = list()
print('**********')

for i in range(len(contacts_list)):
    for j in range(len(contacts_list[i])):
        if (0 <= j <= 1) and (' ' in contacts_list[i][j]):
            tmp = str(contacts_list[i][j]).split(' ')
            for el in tmp:
                tmp_list.append(el)

        elif contacts_list[i][j] != '':
            tmp_list.append(contacts_list[i][j])

    new_list.append(tmp_list)
    tmp_list = []

# pprint(new_list)
#####################################################################
# ВАРИАНТ 1 как хотел уникализировать информацию в списке

# contacts_list_new = (list(set(chain.from_iterable(new_list))))

#####################################################################

#ВАРИАНТ 2 как хотел уникализировать информацию в списке

# my_dict = {}
#
# for my_list in new_list:
#     j = my_list[0]
#     print(j)
#     if j in my_dict.keys():
#         tmp = my_dict.get(j)
#         my_dict[j] = set(tmp) & set([my_list[el] for el in range(len(my_list))])
#
#     else:
#         my_dict[j] = set([my_list[el] for el in range(len(my_list))])
#
#
# pprint(my_dict)
######################################################################

# for k, v in my_dict.items():
#     contacts_list_new.append(k)
#     contacts_list_new.append(list(v))
# #
# pprint(contacts_list_new)

# for i, row in enumerate(new_list):
#     tmp_list = []
#     for j, elem in enumerate(row):
#         print(row)
#         if elem in [el for a_list in contacts_list_new for el in a_list] and j == 0:
#             # for a_list in contacts_list:
#             print(True)
#
#     contacts_list_new.append(row)

# pprint(contacts_list)

# trans = zip(*new_list)
# for el in trans:
#     print(el)

# for i, row in enumerate(new_list):
#     tmp_list = []
#     for j, elem in enumerate(row):
#         if elem in [el for a_list in contacts_list for el in a_list] and j == 0:
#             pos = contacts_list.index(el for a_list in contacts_list for el in a_list)
#             print(pos)
#
#     contacts_list.append(row)

# pprint(contacts_list)
# pattern_telephone = re.compile(r"(\+7|8)?[\s]*\(?(\d+)\)?\s*(\d+)[\s-]*(\d+)[\s-]*(\d+)*(\s?\(?\w{3}\.\s?\d{4}\)?)*")
# text2 = pattern.sub(r"+7-\2-\3-\4-\5", text)

# for elem in contacts_list:
#     for i in range(len(elem)):
#
#         if (i == 0) and (' ' in elem[i]):
#             tmp = str(elem[i]).split(' ')
#             print(tmp)
#             print(
#             type(tmp))
#             print(type(elem))
#             print(type(elem[i]))
#             new_list.extend(tmp)
#
#         else:
#             new_list.append(elem[i])
#
# print('********************')
# pprint(new_list)

# print(elem[])

# TODO 1: выполните пункты 1-3 ДЗ
# ваш код

# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
# with open("phonebook.csv", "w", encoding='UTF-8') as f:
#   datawriter = csv.writer(f, delimiter=',')
#   # Вместо contacts_list подставьте свой список
#   datawriter.writerows(contacts_list)
