# №1 Написать декоратор - логгер. Он записывает в файл дату и время вызова функции,
# имя функции, аргументы, с которыми вызвалась и возвращаемое значение.
# №2 Написать декоратор из п.1, но с параметром – путь к логам.
# №3 Применить написанный логгер к приложению из любого предыдущего д/з.

from datetime import datetime
import time

log = [0, 2, 3, 5, 7, 8, 9]
time_format = "%Y-%m-%d %H:%M:%S"

with open('log.txt', 'w', encoding="UTF-8") as f:
    for i in log:
        now = datetime.now()
        info = f'Число {i} дата и время {now:{time_format}\n}'
        print(info)
        f.write(info)
        # print(f'Число {i} дата и время {now:{time_format}}')
        time.sleep(2)