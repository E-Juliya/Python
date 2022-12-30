# Урок 2. Знакомство с Python. Продолжение
# 1. Напишите программу, которая принимает на вход вещественное число 
# и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

my_j = input('Введите вещественное число: ')
print(my_j)
summa = 0
new_j = my_j.replace('.', '').replace('-','')
print(new_j)
for element in my_j:
    if element.isdigit():
        summa += int(element)


print(summa)


