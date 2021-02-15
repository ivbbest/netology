# №3 Применить написанный логгер к приложению из любого предыдущего д/з.
# честно говоря не могу придумать, как использовать логер для старых д/з, поэтому сделаю простой калькулятор
# и к простым операциям буду применять логгер

from logger import logger_muptiply

@logger_muptiply('log.txt')
def summa(a, b):
    return a + b


@logger_muptiply('log.txt')
def multy(a, b):
    return a * b


@logger_muptiply('log.txt')
def division(a, b):
    return a / b


@logger_muptiply('log.txt')
def pow(a, b):
    return a ** b


@logger_muptiply('log.txt')
def minus(a, b):
    return a - b


@logger_muptiply('log.txt')
def connect(a, b):
    return a + b

if __name__ == '__main__':
    summa(2, 8)
    multy(3, 9)
    pow(13, 6)
    minus(7, 5)
    division(16, 4)
    connect('Hello', ' Python!')
