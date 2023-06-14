# Напишите 5 тестов на функцию all_division. Обязательно должен быть тест деления на ноль.
# Промаркируйте часть тестов. Например, smoke.
# В консоли с помощью pytest сделайте вызов:
# 1) Всех тестов
# 2) Только с маркером smoke
# 3) По маске. Выберите такую маску, чтобы под неё подпадали не все тесты, но больше одного
# Пришлите на проверку файл с тестами и скрины с вызовами и их результаты

import pytest

def all_division(*arg1):

    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division


def test_1():
    assert all_division(1, 4) == 0.25


def test_2():
    with pytest.raises(ZeroDivisionError):
        all_division(1, 0)


def test_my3():
    assert all_division(10) == 10


def test_my4():
    assert all_division(100, 10, 5) == 2


@pytest.mark.smoke
def test_5():
    assert all_division(100, 100) == 1
