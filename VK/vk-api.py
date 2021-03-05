# **Синтаксис любого запроса**
# https://vk.com/dev/api_requests
#
# **Методы**
# https://vk.com/dev/methods
#
# **Версии**
# https://vk.com/dev/versions
#
# **Об ограничениях**
# https://vk.com/dev/api_requests?f=3.%20%D0%9E%D0%B3%D1%80%D0%B0%D0%BD%D0%B8%D1%87%D0%B5%D0%BD%D0%B8%D1%8F%20%D0%B8%20%D1%80%D0%B5%D0%BA%D0%BE%D0%BC%D0%B5%D0%BD%D0%B4%D0%B0%D1%86%D0%B8%D0%B8

# токен и версия api являются обязательными параметрами во всех запросах к vk

import requests
from pprint import pprint

token = '958eb5d439726565e9333aa30e50e0f937ee432e927f0dbd541c541887d919a7c56f95c04217915c32008'


class VkUser:
    url = 'https://api.vk.com/method/'

    def __init__(self, token, version, user_id=''):
        self.token = token
        self.version = version
        self.params = {
            'access_token': self.token,
            'v': self.version
        }
        # self.owner_id = requests.get(self.url+'users.get', self.params).json()['response'][0]['id']
        self.user_id = user_id

    def __and__(self, other):
        '''Найти общих друзей'''
        resp1 = self.get_friends()
        resp2 = other.get_friends()
        common = []
        for item in resp1['response']['items']:
            if item in resp2['response']['items']:
                common.append(item)
        return common

    # получим своих подписчиков при помощи [users.getFollowers](https://vk.com/dev/users.getFollowers)
    def get_followers(self):
        followers_url = self.url + 'users.getFollowers'
        followers_params = {
            'count': 1000,
            'user_id': self.user_id
        }
        res = requests.get(followers_url, params={**self.params, **followers_params})
        return res.json()

    # Получим базовую информацию о пользователе при помощи [users.get](https://vk.com/dev/users.get)
    def get_groups(self):
        groups_url = self.url + 'groups.get'
        groups_params = {
            'count': 1000,
            'user_id': self.user_id,
            'extended': 1,
            'fields': 'members_count'
        }
        res = requests.get(groups_url, params={**self.params, **groups_params})
        return res.json()

    # Получим базовую информацию о пользователе при помощи [users.get](https://vk.com/dev/users.get)
    def users_get(self):
        users_url = self.url + 'users.get'
        user_params = {
            'count': 1000,
            'user_id': self.user_id,
        }
        res = requests.get(users_url, params={**self.params, **user_params})
        return res.json()

    # Получим базовую информацию о пользователе при помощи [friends.get](https://vk.com/dev/friends.get)
    def get_friends(self):
        '''Получить список друзей'''
        users_url = self.url + 'friends.get'
        user_params = {
            'user_id': self.user_id,
        }
        res = requests.get(users_url, params={**self.params, **user_params})
        return res.json()

    def get_status(self):
        '''Получить статус пользователя'''
        users_url = self.url + 'status.get'
        user_params = {
            'user_id': self.user_id,
        }
        res = requests.get(users_url, params={**self.params, **user_params})
        return res.json()

    def set_status(self, text):
        '''Установка статуса пользователя'''
        users_url = self.url + 'status.get'
        user_params = {
            'user_id': self.user_id,
            'text': text
        }
        res = requests.get(users_url, params={**self.params, **user_params})

        return res.json()

    def __repr__(self):
        return 'https://vk.com/id' + str(self.user_id)


def url_from_id(user_id):
    """Сделать id пользователя готовым урлом"""
    if str(user_id).isdigit():
        url = f'https://vk.com/id{user_id}'
    else:
        url = f'https://vk.com/{user_id}'

    return url


if __name__ == '__main__':
    usr1 = VkUser(token, '5.126', '15871719')
    # pprint(usr1.friends_get())
    usr2 = VkUser(token, '5.126', '138611543')
    # pprint(usr2.friends_get())
    # print(usr1 & usr2)
    for elem in usr1 & usr2:
        print(url_from_id(elem))
