# Написать генератор, который принимает путь к файлу. При каждой итерации возвращает md5 хеш каждой строки файла.

import json
import hashlib


def hash_analysis(file):
    i = 0
    with open(file, encoding='utf-8') as f:
        data = f.readlines()

    while i < len(data):
        my_hash = hashlib.md5(str(data[i]).encode())
        yield my_hash.hexdigest()
        i += 1


if __name__ == '__main__':
    for hash_md5 in hash_analysis('test.txt'):
        print(hash_md5)