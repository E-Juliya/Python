# Урок 2. Знакомство с Python. Продолжение
# 3. Реализуйте алгоритм перемешивания списка. НЕ ИСПОЛЬЗОВАТЬ 
# ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE, максимум использование библиотеки 
# Random для получения случайного int

import math
from random import randint as RI

my_list = [i for i in range(10)]

def my_shuffle(new_list: list):
    for i in range(len(new_list)):
        ni = RI(0,len(new_list) - 1)
        new_list.append(new_list.pop(ni))

print(my_list)
my_shuffle(my_list)
print(my_list)
