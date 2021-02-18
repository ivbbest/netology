# Проверим правильность работы Яндекс.Диск REST API. Написать тесты, проверяющий создание папки на Диске.
# Используя библиотеку requests напишите unit-test на верный ответ и возможные отрицательные тесты на ответы с ошибкой
#
# Пример положительных тестов:
#
# Код ответа соответствует 200.
# Результат создания папки - папка появилась в списке файлов.


import unittest
from yandexdisk import YaUploader


class TestYandexDisk(unittest.TestCase):

    # корректный токен

    token = {"Authorization": "OAuth AgAAAAAZhU-gAADLWwQPbEqXgkAQt0catuijfnk"}

    # некорректный токен

    token1 = {"Authorization": "OAuth AgAAAAAZhU-gAADLWwQPbEijfnk"}

    # длинное название

    trash = 'API отвечает кодом 201 Created (папка успешно создана). ' \
            'В теле ответа, в объекте Link, возвращается ссылка на мета-информацию о созданном ресурсе.Если ' \
            'запрос был обработан без ошибок, API отвечает кодом 201 Created (папка успешно создана). В теле ' \
            'ответа, в объекте Link, возвращается ссылка на мета-информацию о созданном ресурсе.'

    def setUp(self):
        self.ya = YaUploader()

    def test_yandex_ok(self):
        answer = self.ya.create_dir_ya('88', self.token)
        self.assertEqual(answer, 201)
        print('Все создано')

    def test_yandex_409(self):
        answer1 = self.ya.create_dir_ya('new', self.token)
        self.assertEqual(answer1, 409)
        print('Такая папка уже создана')

    def test_yandex_401(self):
        answer2 = self.ya.create_dir_ya(self.trash, self.token1)
        self.assertEqual(answer2, 401)
        print('Не удалось найти запрошенный ресурс.')


if __name__ == "__main__":
    unittest.main()