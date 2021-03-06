import requests
import os


class YaUploader:
    def __init__(self, token):
        self.token = token

    def create_dir(self, my_dir):
        """Метод создает папку my_dir на яндекс диск"""

        response = requests.put('https://cloud-api.yandex.net/v1/disk/resources',
                                params={"path": my_dir},
                                headers=self.token)

        return response.status_code

    def upload(self, file: str, directory='/'):
        """Метод загружает файл file на яндекс диск"""

        if directory != '/':
            directory = directory + '/'

        resp = requests.get(
        "https://cloud-api.yandex.net/v1/disk/resources/upload",
        headers=self.token,
        params={"path": f'{directory}{file}'}
        )

        put_url = resp.json().get('href')
        print(put_url)
        files = {'file': open(f'images/{file}', 'rb')}

        response = requests.put(put_url, files=files, headers=self.token)
        print(response)
        return 'Вернуть ответ об успешной загрузке'


if __name__ == '__main__':
    token = {"Authorization": "OAuth AgAEA7qiJubnAADLW5Yd-GCDLkW4iWW1iQbIkCk"}
    directory = 'vk'
    uploader = YaUploader(token)
    status_dir = uploader.create_dir(directory)
    print(status_dir)
    if 200 <= status_dir <= 201 or status_dir == 409:
        images = os.listdir('images')
        print(images)
        for image in images:
            uploader.upload(image, directory)
