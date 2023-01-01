#Урок 3. Данные, функции и модули в Python
# 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу 
# между максимальным и минимальным значением дробной части элементов, отличной от 0.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19
import math
from random import randint as RI
from random import uniform as uf

myList = [round(uf(0, 100), RI(0,3)) for _ in range(10)]
for _ in range(len(myList)):
    item = myList.pop(0)
    myList.append(item if item != int(item) else int(item))
print(myList)
newList = []

for item in myList:
    if item != int(item):
        newList.append(round(item%1, 3))

print(newList)

print(f'Разница между максимальной({max(newList)}) и минимальной ({min(newList)}) дробными частями будет {max(newList) - min(newList)}')