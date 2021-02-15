# №1 Написать декоратор - логгер. Он записывает в файл дату и время вызова функции,
# имя функции, аргументы, с которыми вызвалась и возвращаемое значение.
# №2 Написать декоратор из п.1, но с параметром – путь к логам.
# №3 Применить написанный логгер к приложению из любого предыдущего д/з.

from datetime import datetime
import time


def logger_muptiply(log):
    def logger(old_func):
        time_format = "%Y-%m-%d %H:%M:%S"

        def new_function(*args, **kwargs):
            with open(log, 'a', encoding="UTF-8") as f:
                result = old_func(*args, **kwargs)
                now = datetime.now()
                info = f"Дата и время вызова функции {now:{time_format}}, ее имя - {old_func.__name__}, " \
                       f"аргументы ({args} {kwargs}), результат - {result}\n"
                print(info)
                f.write(info)
                time.sleep(2)

            return result

        return new_function

    return logger


@logger_muptiply('log.txt')
def summa(a, b):
    return a + b

if __name__ == '__main__':
    summa(2, 8)
    summa(3, 9)
    summa(13, 6)
    summa(7, 5)