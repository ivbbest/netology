# Проверим правильность работы Яндекс.Диск REST API. Написать тесты, проверяющий создание папки на Диске.
# Используя библиотеку requests напишите unit-test на верный ответ и возможные отрицательные тесты на ответы с ошибкой
#
# Пример положительных тестов:
#
# Код ответа соответствует 200.
# Результат создания папки - папка появилась в списке файлов.

import requests


class YaUploader:
    # def __init__(self, token):
    #     self.token = token

    def create_dir_ya(self, my_dir, token):
        """Метод загруджает файл file_path на яндекс диск"""

        # resp = requests.get(
        # "https://cloud-api.yandex.net/v1/disk/resources/upload",
        # headers=self.token,
        # params={"path": file}
        # )

        # put_url = resp.json().get('href')
        # print(put_url)
        #
        # files = {'file': open(file, 'rb')}

        response = requests.put('https://cloud-api.yandex.net/v1/disk/resources',
                                params={"path": my_dir},
                                headers=token)
        return response.status_code

        # return 'Вернуть ответ об успешной загрузке'


if __name__ == '__main__':
    token = {"Authorization": "OAuth ***"}
    uploader = YaUploader()
    result = uploader.create_dir_ya('5', token)
    print(result)


