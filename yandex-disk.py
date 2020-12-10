import requests
import os
from pprint import pprint

HEADERS = {"Authorization": "OAuth mytoken"}
#
# class YaUploader:
#     def __init__(self, token):
#         self.token = token
#
#     def upload(self, file_path: str):
#         """Метод загруджает файл file_path на яндекс диск"""
#         resp = requests.get("https://cloud-api.yandex.net/v1/disk/resources/upload", params={"path" : "/"})
#         print(resp)
#         return 'Вернуть ответ об успешной загрузке'
#
#
# if __name__ == '__main__':
#     token = 'AgAAAAAZhU-gAADLWwQPbEqXgkAQt0catuijfnk'
#     uploader = YaUploader(token)
#     result = uploader.upload('c:\my_folder\file.txt')


# resp = requests.get(
#     "https://cloud-api.yandex.net/v1/disk/resources/",
#     params={"path": "/"},
#     headers=HEADERS,
# )
file = 'file.txt'

if os.path.isfile(file):
    with open(file, encoding='UTF-8') as f:
        resp = requests.get(
            "https://cloud-api.yandex.net/v1/disk/resources/upload",
            headers=HEADERS,
            params={"path": file},
        )

        data = resp.json()
        # pprint(data)
        print(data['href'])

        upload_file = requests.put(
            data['href'],
            params={"path": file},
            headers=HEADERS,

        )


        print(upload_file.raise_for_status())