# Задача 1
# Необходимо парсить страницу со свежими статьями (вот эту) и выбирать те статьи, в которых встречается
# хотя бы одно из ключевых слов (эти слова определяем в начале скрипта). Поиск вести по всей доступной
# preview-информации (это информация, доступная непосредственно с текущей страницы).
# Вывести в консоль список подходящих статей в формате: <дата> - <заголовок> - <ссылка>.

# Задача 2
# Улучшить скрипт так, чтобы он анализировал не только preview-информацию статьи, но и весь текст статьи целиком.
# Для этого потребуется получать страницы статей и искать по тексту внутри этой страницы.
# https://github.com/netology-code/py-homeworks-advanced/tree/master/6.Web-scrapping


import requests
from bs4 import BeautifulSoup

# определяем список хабов, которые нам интересны
KEYWORDS = ['дизайн', 'фото', 'web', 'python', 'javascript']


def init_info_habr():
    '''
    Инициализация работы с основным урлом хабры, где все свежие посты.
    '''
    # получаем страницу с самыми свежими постами
    ret = requests.get('https://habr.com/ru/all/')
    soup = BeautifulSoup(ret.text, 'html.parser')
    # извлекаем посты
    posts = soup.find_all('article', class_='post')

    return posts


def full_url_info():
    '''
    Получение списка урлов всех свежих постов в Хабре
    '''
    posts = init_info_habr()
    href_list = list()

    for post in posts:
        title_element = post.find('a', class_='post__title_link')
        href = title_element.attrs.get('href')
        href_list.append(href)

    return href_list


def search_key_in_preview():
    '''
    Поиск ключей в превью постов на хабре. Задача №1
    '''
    posts = init_info_habr()
    articles = list()

    for post in posts:
        if any([desired in post.text.lower() for desired in KEYWORDS]):
            time = post.find('span', class_='post__time').text
            title_element = post.find('a', class_='post__title_link')
            title = title_element.text
            href = title_element.attrs.get('href')
            art = f'{time} - {title} - {href}'
            articles.append(art)

    if len(articles) > 0:
        for elem in articles:
            print(elem)
    else:
        print('Статей с заданными ключами не найдено')


def search_key_in_articles():
    '''
    Поиск ключей в полной статье на хабре. Задача №2
    '''
    list_url = full_url_info()
    articles = list()

    for href in list_url:
        ret = requests.get(href)
        soup = BeautifulSoup(ret.text, 'html.parser')
        # извлекаем посты
        post = soup.find('article', class_='post')

        if any([desired in post.text.lower() for desired in KEYWORDS]):
            time = post.find('span', class_='post__time').text
            title = post.find('span', class_='post__title-text').text
            art = f'{time} - {title} - {href}'
            articles.append(art)

    if len(articles) > 0:
        for elem in articles:
            print(elem)
    else:
        print('Статей с заданными ключами не найдено')


if __name__ == '__main__':
    # search_key_in_preview()
    search_key_in_articles()