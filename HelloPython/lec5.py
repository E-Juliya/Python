# Напишите программу вычисления арифметического выражения заданного строкой. 
# Используйте операции +,-,/,*. приоритет операций стандартный. 
# *Пример:*   2+2 => 4;     1+2*3 => 7;     1-2*3 => -5;

string01 = '1+2*3'
new_string01 = string01.replace('+', ' ').replace('*', ' ').replace('/', ' ').replace('-', ' ')
print(new_string01)

string02 = string01.replace('0', ' ').replace('1', ' ').replace('2', ' ').replace('3', ' ')\
    .replace('4', ' ').replace('5', ' ').replace('6', ' ').replace('7', ' ')\
        .replace('8', ' ').replace('9', ' ')
print(string02)
#new_string = [x for x in new_string01 ]
