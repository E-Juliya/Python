#Урок 3. Данные, функции и модули в Python
#1.Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму 
#элементов списка, стоящих на позиции с нечетным индексом.
#Пример:
#[2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
import math
from random import randint as RI
from datetime import datetime

myList = [RI (1, 10) for i in range(15)]
summa = 0
start = datetime.timestamp(datetime.now())
for i in range(1, len(myList), 2):
    summa += myList[1]

print(myList)
print(datetime.timestamp(datetime.now()) - start)