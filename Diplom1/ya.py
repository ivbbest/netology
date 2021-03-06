import requests


class YaUploader:
    def __init__(self, token):
        self.token = token

    def create_dir(self, my_dir):
        """Метод создает папку my_dir на яндекс диск"""

        response = requests.put('https://cloud-api.yandex.net/v1/disk/resources',
                                params={"path": my_dir},
                                headers=self.token)
        return response.status_code

    def upload(self, file: str):
        """Метод загружает файл file на яндекс диск"""

        resp = requests.get(
        "https://cloud-api.yandex.net/v1/disk/resources/upload",
        headers=self.token,
        params={"path": f'v/{file}'}
        )

        put_url = resp.json().get('href')
        print(put_url)
        files = {'file': open(file, 'rb')}

        response = requests.put(put_url, files=files, headers=self.token)
        print(response)
        return 'Вернуть ответ об успешной загрузке'


if __name__ == '__main__':
    token = {"Authorization": "OAuth AgAEA7qiJubnAADLW5Yd-GCDLkW4iWW1iQbIkCk"}
    uploader = YaUploader(token)
    # result = uploader.create_dir('v')
    result2 = uploader.upload('file.txt')
    print(result2)
