#вариант решения от Александра Бардина
import requests
from pprint import pprint

TOKEN = '958eb5d439726565e9333aa30e50e0f937ee432e927f0dbd541c541887d919a7c56f95c04217915c32008'

class User:
    def __init__(self, token, user_id=''):
        self.token = token
        self.user_id = user_id

    def __and__(self, other):
        resp1 = self.get_friends()
        resp2 = other.get_friends()
        common = []
        for item in resp1['response']['items']:
            if item in resp2['response']['items']:
                common.append(item)
        return common

    def get_status(self):
        response = requests.get(
            'https://api.vk.com/method/status.get',
            params={
                'access_token': self.token,
                'v': 5.103
            }
        )
        return response.json()

    def set_status(self, text):
        response = requests.get(
            'https://api.vk.com/method/status.set',
            params={
                'access_token': self.token,
                'v': 5.103,
                'text': text
            }
        )
        return response.json()

    def __repr__(self):
        return 'https://vk.com/id' + str(self.user_id)

    def get_friends(self):
        response = requests.get(
            'https://api.vk.com/method/friends.get',
            params={
                'access_token': self.token,
                'v': 5.103,
                'user_id': self.user_id
            }
        )
        return response.json()

if __name__ == '__main__':

    Anna = User(TOKEN, '15871719')
    pprint(Anna.get_friends())
    Petya = User(TOKEN, '138611543')
    pprint(Anna & Petya)
    pprint(Anna)
    pprint(Petya)