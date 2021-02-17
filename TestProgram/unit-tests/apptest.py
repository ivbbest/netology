# Задача №1 unit-tests
# Задание http://joxi.ru/4Ak5b4Zskq9v6m или https://github.com/netology-code/py-homeworks-advanced/tree/master/4.Tests


from unittest import TestCase
from unittest.mock import patch
from app import get_doc_owner_name


class TestApp(TestCase):

    @patch('app.get_doc_owner_name', sid)
    def test_get_doc_owner_name(self):
        pass
