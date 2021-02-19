# Задача №1 unit-tests
# Задание http://joxi.ru/4Ak5b4Zskq9v6m или https://github.com/netology-code/py-homeworks-advanced/tree/master/4.Tests


from unittest import TestCase
from unittest.mock import patch
from app import get_doc_owner_name, check_document_existance, delete_doc, get_doc_shelf, \
    add_new_shelf, remove_doc_from_shelf
from unittest import TestCase, mock, main


class TestApp(TestCase):

    @mock.patch('app.input')
    def test_get_doc_owner_name(self, mock_doc_number):
        mock_doc_number.return_value = '10006'
        result = get_doc_owner_name()
        self.assertEqual("Аристарх Павлов", result)

    @mock.patch('app.input')
    def test_add_new_shelf(self, mock_shelf):
        mock_shelf.return_value = '5'
        result = add_new_shelf()
        self.assertEqual(('5', True), result)

    @mock.patch('app.input')
    def test_add_new_shelf2(self, mock_shelf2):
        mock_shelf2.return_value = '2'
        result = add_new_shelf()
        self.assertEqual(('2', False), result)

    @mock.patch('app.input')
    def test_get_doc_shelf(self, mock_doc_number):
        mock_doc_number.return_value = '10006'
        result = get_doc_shelf()
        self.assertEqual('2', result)

    @mock.patch('app.input')
    def test_delete_doc(self, mock_doc_number):
        mock_doc_number.return_value = '11-2'
        result = delete_doc()
        self.assertEqual(('11-2', True), result)

    @mock.patch('app.check_document_existance')
    def test_check_document_existance(self, mock_doc_number):
        mock_doc_number.return_value = True
        document = '11-2'
        result = check_document_existance(document)
        self.assertEqual(result, True)

    @mock.patch('app.remove_doc_from_shelf')
    def test_remove_doc_from_shelf(self, mock_doc_number):
        mock_doc_number.return_value = True
        document = '10006'
        result = remove_doc_from_shelf(document)
        self.assertEqual(result, True)


if __name__ == '__main__':
    main()