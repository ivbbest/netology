import json
# import requests

# Написать класс итератора, который по каждой стране из файла countries.json ищет страницу из википедии.
# Записывает в файл пару: страна – ссылка. Ссылку формировать самостоятельно.

# работа программы с использованием класса


class MyJson:

    def __init__(self, file, start):
        self.wiki = 'https://en.wikipedia.org/wiki/'
        self.start = start - 1
        with open(file, encoding='utf-8') as f:
            self.json_data = json.load(f)

    def __iter__(self):
        return self

    def __next__(self):
        self.start += 1
        if self.start == len(self.json_data):
            raise StopIteration
        country = self.json_data[self.start]['name']['common']
        country_url = country
        if ' ' in country:
            country_url = str(country).replace(' ', '_')

        url = f'{self.wiki}{country_url}'
        result = f'{country} - {url}'

        # Если требуется проверка статуса кода урла, то можно использовать библиотеку requests
        # При этом программа работает долго из-за внешних запросов.

        # response = requests.get(url)
        # if response.status_code == 200:
        #     result = f'{country} - {url}'
        #
        # else:
        #     result = f'В Википедии страны {country} по урлу {url} не найдено'

        return result

if __name__ == '__main__':
    for line in MyJson('countries.json', 0):
        print(line)


#работа программы без классов

# file = 'countries.json'
# wiki = 'https://en.wikipedia.org/wiki/'
#
# with open(file, encoding='utf-8') as f:
#     json_data = json.load(f)
#
# # len_json = len(json_data['name']['name']['common'])
#
# # pprint(json_data)
# # print(json_data['name'])
# print(len(json_data))
# print(type(json_data))
#
# for i in range(len(json_data)):
#     country = json_data[i]['name']['common']
#     country_url = country
#     if ' ' in country:
#         country_url = str(country).replace(' ', '_')
#
#     url = f'{wiki}{country_url}'
#     result = f'{country} - {url}'
#     print(result)