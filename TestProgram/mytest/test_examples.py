from unittest import TestCase, mock, main
from examples import get_number

class GetNumberTests(TestCase):

    @mock.patch('examples.randint')
    def test_get_number_with_even_number(self, randint_mock):
        randint_mock.return_value = 42
        result = get_number()
        self.assertEqual('Even number: 42', result)

    @mock.patch('examples.randint')
    def test_get_number_with_odd_number(self, randint_mock):
        randint_mock.return_value = 69
        result = get_number()
        self.assertEqual('Odd number: 69', result)


if __name__ == '__main__':
    main()