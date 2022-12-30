# Урок 2. Знакомство с Python. Продолжение
# 2. Задайте список из n чисел последовательности (1 + 1/n)**n, 
# выведеите его на экран, а так же сумму элементов списка.
# Пример:
# Для n=4 -> [2, 2.25, 2.37, 2.44]
# Сумма 9.06

n = int(input("Введите целое число: "))
my_list = []
for i in range(1, n+1):
    my_list.append(round((1+1/i)**i, 2))
print(f'При n={n} список будет {my_list},')
print(f'а его сумма {sum(my_list)}')