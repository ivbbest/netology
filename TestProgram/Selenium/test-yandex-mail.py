# Применив selenium, напишите unit-test для авторизации на Яндексе по url: https://passport.yandex.ru/auth/

import unittest
from yandex_auth import auth_yandex_mail, init_selenium


class TestYandex(unittest.TestCase):

    def setUp(self):
        self.browser = init_selenium()

    def test_yandex_mail1(self):
        assert auth_yandex_mail('test', 'test') == 'OK', 'Error'

    def test_yandex_mail2(self):
        assert auth_yandex_mail('login', 'password') == 'OK', 'Error'

    def tearDown(self):
        self.browser.close()


if __name__ == "__main__":
    unittest.main()