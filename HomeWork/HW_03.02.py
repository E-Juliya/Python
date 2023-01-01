#Урок 3. Данные, функции и модули в Python
#2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем 
# первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]
import math
from random import randint as RI

myList = [RI (1, 10) for i in range(6)]
newList = []
for i in range(len(myList)//2):
    newList.append(myList[i]*myList[-i-1])

if len(myList) % 2 != 0:
    newList.append(myList[len(myList)//2]**2)

print(myList)
print(newList)

