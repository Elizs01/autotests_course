# Напишите декоратор func_log, который может принимать аргумент file_log (Путь до файла), по умолчнию равен 'log.txt'
# Декоратор должен дозаписывать в файл имя вызываемой функции (можно получить по атрибуту __name__), дату и время вызова
# по формату:
# имя_функции вызвана %d.%m %H:%M:%S
# Для вывода времени нужно использовать модуль datetime и метод .strftime()
# https://pythonworld.ru/moduli/modul-datetime.html
# https://docs.python.org/3/library/datetime.html
#
# Например
# @func_log()
# def func1():
#     time.sleep(3)
#
# @func_log(file_log='func2.txt')
# def func2():
#     time.sleep(5)
#
# func1()
# func2()
# func1()
#
# Получим:
# в log.txt текст:
# func1 вызвана 30.05 14:12:42
# func1 вызвана 30.05 14:12:50
# в func2.txt текст:
# func2 вызвана 30.05 14:12:47

# Со звёздочкой. ДЕЛАТЬ НЕ ОБЯЗАТЕЛЬНО.
# help(func1) должен выводит одинаковый текст, когда есть декоратор на функции func1 и когда его нет
# Реализовать без подключения новых модулей и сторонних библиотек.

# Здесь пишем код
from datetime import datetime
from pathlib import Path
import time

def func_log(file_log='log.txt'):
    """
    Запись в файл названия функции и текущей даты и времени
    :param file_log: название файла в который выполняется запись
    """
    def writefunc(func):
        func()
        f = open(Path(Path.cwd(), file_log), mode='r+', encoding='utf-8')
        datetimenow = datetime.strftime(datetime.today(), "%d.%m %H:%M:%S")
        f.seek(0, 2)
        f.write(f"{func.__name__} вызвана {datetimenow}\n")
    return writefunc


@func_log()
def func1():
    time.sleep(3)


@func_log(file_log='func2.txt')
def func2():
    time.sleep(5)

func1()
func2()
func2()
func1()
