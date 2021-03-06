import requests
from pprint import pprint
from datetime import datetime
from progress.bar import Bar

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

    def photos_get(self):
        '''Получение json файла с информацией о фото по user_id'''
        users_url = self.url + 'photos.get'
        user_params = {
            'user_id': self.user_id,
            'album_id': 'profile',
            'extended': 1,
            'photo_sizes': 1
        }
        res = requests.get(users_url, params={**self.params, **user_params})
        return res.json()

    def photos_get_url(self):
        '''Разбор json photos_get с получением на выходе списка из кортежей, в которых указано:
        количество лайков, url картинки из профиля и дата загрузки'''
        json_info = self.photos_get()
        photo_all_info = list()
        for info_photo in json_info['response']['items']:
            for photo in info_photo['sizes']:
                if photo['type'] == 'z':
                    likes = info_photo['likes']['count']
                    date = datetime.fromtimestamp(int(info_photo['date'])).strftime('%Y-%m-%d')
                    url = photo['url']
                    tmp_data = likes, url, date
                    photo_all_info.append(tmp_data)

        return photo_all_info

    def save_photo_to_disk(self):
        '''Сохранение картинок из ВК на компьютер.'''
        photo_info = self.photos_get_url()
        set_likes = set()
        list_photo_file = list()

        # Добавил прогресс бар, чтобы в терминале видеть процесс работы
        with Bar('Processing', max=len(photo_info)) as bar:
            for photo in photo_info:
                name = photo[0]
                #подумать тут дублей названий не может быть, потому что всегда добавляется дата фото
                # а нужно делать название лайки и если столько лайков есть для другого фото,
                # то тогда только добавлять дату

                if name not in set_likes:
                    name = f'{name}{photo[2]}'
                set_likes.add(name)

                url = requests.get(photo[1])
                with open(f'images/{name}.jpg', 'wb') as f:
                    f.write(url.content)
                    list_photo_file.append({"file_name": f'{name}.jpg', "size": "z"})
                    bar.next()

        return list_photo_file

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


if __name__ == '__main__':
    usr1 = VkUser(token, '5.126', '15871719')
    pprint(usr1.save_photo_to_disk())
