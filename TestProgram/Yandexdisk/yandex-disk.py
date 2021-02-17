import requests


class YaUploader:
    def __init__(self, token):
        self.token = token

    def upload(self, file: str):
        """Метод загруджает файл file_path на яндекс диск"""

        resp = requests.get(
        "https://cloud-api.yandex.net/v1/disk/resources/upload",
        headers=self.token,
        params={"path": file}
        )

        put_url = resp.json().get('href')
        print(put_url)

        files = {'file': open(file, 'rb')}

        response = requests.put(put_url, files=files, headers=self.token)
        print(response)
        return 'Вернуть ответ об успешной загрузке'


if __name__ == '__main__':
    token = {"Authorization": "OAuth AgAAAAAZhU-gAADLWwQPbEqXgkAQt0catuijfnk"}
    uploader = YaUploader(token)
    result = uploader.upload('file.txt')


