#Урок 1. Знакомство с Python
# Напишите программу, которая принимает на вход координаты двух точек и 
# находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

num_AX = int(input('Введите координату X точки А: '))
num_AY = int(input('Введите координату Y точки А: '))
a = num_AX, num_AY
num_BX = int(input('Введите координату X точки B: '))
num_BY = int(input('Введите координату Y точки B: '))
b = num_BX, num_BY
print(a, b)
from math import sqrt
S = sqrt((num_AX - num_BX) * (num_AX - num_BX) + (num_AY - num_BY) * (num_AY - num_BY))
print(S)


