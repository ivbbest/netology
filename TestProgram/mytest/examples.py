# examples.py
from random import randint


def get_number():
    number = randint(1, 100)
    if number % 2 == 0:
        return 'Even number: {}'.format(number)
    return 'Odd number: {}'.format(number)

if __name__ == '__main__':
    print(get_number())