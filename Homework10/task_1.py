# Напишите генератор generate_random_name(), используя модуль random,
# который генерирует два слова из латинских букв от 1 до 15 символов, разделенных пробелами
# Например при исполнении следующего кода:
# gen = generate_random_name()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
#
# Выводится:
# tahxmckzexgdyt ocapwy
# dxqebbukr jg
# aym jpvezfqexlv
# iuy qnikkgxvxfxtxv

import random
import string
from random import randint

# Здесь пишем код
def generate_random_name():
    """
    Генерирует два слова
    """
    generate_name = ""
    for i in range(2):
        generate_name += ''.join(random.choices(string.ascii_lowercase, k=randint(1, 15))) + " "
    yield generate_name

