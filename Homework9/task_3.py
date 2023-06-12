# Дан файл test_file/task_3.txt можно считать, что это запись покупок в магазине, где указана только цена товара
# В каждой строке файла записана цена товара.
# Покупки (т.е. несколько подряд идущих цен) разделены пустой строкой
# Нужно найти сумму трёх самых дорогих покупок, которые запишутся в переменную three_most_expensive_purchases

# Здесь пишем код
from pathlib import Path
price_commodity = open(Path(Path.cwd(), "test_file/task_3.txt"), "r", encoding='utf-8').readlines()
summ = 0
summ_commodity = []
for price in price_commodity:
    if price != "\n":
        summ += int(price)
    else:
        summ_commodity.append(summ)
        summ = 0
summ_commodity.sort()
three_most_expensive_purchases = summ_commodity[-1] + summ_commodity[-2] + summ_commodity[-3]
assert three_most_expensive_purchases == 202346