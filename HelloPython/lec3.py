# 18.12
#3. Напишите программу, которая определит позицию второго вхождения строки в списке 
# либо сообщит, что её нет.
#*Пример:*
#- список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
#- список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
#- список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
#- список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
#- список: [], ищем: "123", ответ: -1
def f(x):
    return x**2
j = 1, 2, 3, 5, 8, 15, 23, 38
list = [(i, f(i)) for i in j if i%2 ==0]
print(list)