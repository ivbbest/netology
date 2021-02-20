from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv
import re


with open("phonebook_raw.csv", encoding='UTF-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

pprint(str(contacts_list[1][0]).split(' '))
pprint(contacts_list)


new_list = list()
new_list.append(contacts_list[0])
len_contacts_list = len(contacts_list)
print('**********')
# for elem in contacts_list:
#     for i in range(len(elem)):
#
#         if (i == 0) and (' ' in elem[i]):
#             tmp = str(elem[i]).split(' ')
#             # print(tmp)
#             # print(type(tmp))
#             # print(type(elem))
#             # print(type(elem[i]))
#             new_list.extend(tmp)
#
#         else:
#             new_list.append(elem[i])
#
# print('********************')
# pprint(new_list)

    # print(elem[])
for i in range(1, len_contacts_list):
    for j in range(len(contacts_list[i])):
        if (0 <= j <= 1) and (' ' in contacts_list[i][j]):
            tmp = str(contacts_list[i][j]).split(' ')
            new_list.append(tmp)

        elif contacts_list[i][j] == '':
            continue
        else:
            new_list.append(contacts_list[i][j])


pprint(new_list)
# pattern_telephone = re.compile(r"(\+7|8)?[\s]*\(?(\d+)\)?\s*(\d+)[\s-]*(\d+)[\s-]*(\d+)*(\s?\(?\w{3}\.\s?\d{4}\)?)*")
# text2 = pattern.sub(r"+7-\2-\3-\4-\5", text)

# TODO 1: выполните пункты 1-3 ДЗ
# ваш код

# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
# with open("phonebook.csv", "w", encoding='UTF-8') as f:
#   datawriter = csv.writer(f, delimiter=',')
#   # Вместо contacts_list подставьте свой список
#   datawriter.writerows(contacts_list)
