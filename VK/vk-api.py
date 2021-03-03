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


token = '958eb5d439726565e9333aa30e50e0f937ee432e927f0dbd541c541887d919a7c56f95c04217915c32008'


class VkUser:
    url = 'https://api.vk.com/method/'

    def __init__(self, token, version):
        self.token = token
        self.version = version
        self.params = {
            'access_token': self.token,
            'v': self.version
        }
        self.owner_id = requests.get(self.url+'users.get', self.params).json()['response'][0]['id']
        self.friends = []

    # def __and__(self, other):
    #     user1 = VkUser(self, self.token, self.version)
    #     user2 = VkUser(other, self.token, self.version)
    #
    #     return user1 & user2

    # получим своих подписчиков при помощи [users.getFollowers](https://vk.com/dev/users.getFollowers)
    def get_followers(self, user_id=None):
        if user_id is None:
            user_id = self.owner_id
        followers_url = self.url + 'users.getFollowers'
        followers_params = {
            'count': 1000,
            'user_id': user_id
        }
        res = requests.get(followers_url, params={**self.params, **followers_params})
        return res.json()

    # Получим базовую информацию о пользователе при помощи [users.get](https://vk.com/dev/users.get)
    def get_groups(self, user_id=None):
        if user_id is None:
            user_id = self.owner_id
        groups_url = self.url + 'groups.get'
        groups_params = {
            'count': 1000,
            'user_id': user_id,
            'extended': 1,
            'fields': 'members_count'
        }
        res = requests.get(groups_url, params={**self.params, **groups_params})
        return res.json()

    # Получим базовую информацию о пользователе при помощи [users.get](https://vk.com/dev/users.get)
    def users_get(self, user_id=None):
        if user_id is None:
            user_id = self.owner_id
        users_url = self.url + 'users.get'
        user_params = {
            'count': 1000,
            'user_id': user_id,
        }
        res = requests.get(users_url, params={**self.params, **user_params})
        return res.json()


    # Получим базовую информацию о пользователе при помощи [friends.get](https://vk.com/dev/friends.get)
    def friends_get(self, user_id=None):
        if user_id is None:
            user_id = self.owner_id
        users_url = self.url + 'friends.get'
        user_params = {
            'user_id': user_id,
        }
        res = requests.get(users_url, params={**self.params, **user_params})
        return res.json()['response']['items']

    #поиск общих друзей из 2 пользователей
    def mutual_friends(self, user_id1=None, user_id2=None):
        if user_id1 is None:
            user_id1 = self.owner_id

        if user_id2 is None:
            user_id2 = self.owner_id

        if user_id1 == user_id2:
            return 'Вы ввели некорректные данные пользователей, у которых требуется найти общих друзей!!!\n'

        else:
            self.friends = list(set(self.friends_get(user_id1)) & \
                   set(self.friends_get(user_id2)))

            # return self.friends


           # friend1 = set(self.friends_get(user_id1)['response']['items'])
           # friend2 = set(self.friends_get(user_id2)['response']['items'])
           # common_friends = list(set(friend1) & set(friend2))
           # for friend in common_friends:
           #     if str(friend).isdigit():
           #         print(f'https://vk.com/id{friend}')
           #
           #     else:
           #         print(f'https://vk.com/{friend}')

    def __str__(self):
        for friend in self.friends:

            if str(friend).isdigit():
               return f'https://vk.com/id{friend}'

            else:
               return f'https://vk.com/{friend}'


if __name__ == '__main__':
    vk_client = VkUser(token, '5.126')
    #print(vk_client.get_groups())
    #print(vk_client.friends_get())
    common_friends = vk_client.mutual_friends(15871719, 138611543)
    print(common_friends)
    # print(vk_client.search_query('python'))