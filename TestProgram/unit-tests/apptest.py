# Задача №1 unit-tests
# Задание http://joxi.ru/4Ak5b4Zskq9v6m или https://github.com/netology-code/py-homeworks-advanced/tree/master/4.Tests


from unittest import TestCase
from unittest.mock import patch
from app import get_doc_owner_name


class TestApp(TestCase):

    @patch('app.get_doc_owner_name', return_value="Василий Гупкин")
    def test_get_doc_owner_name(self):
        pass

# https://queirozf.com/entries/python-unittest-examples-mocking-and-patching - почитать
# https://medium.com/@yeraydiazdiaz/what-the-mock-cheatsheet-mocking-in-python-6a71db997832
# https://hacksoft.io/mock-everything/
