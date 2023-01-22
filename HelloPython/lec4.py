#14.01 
# В файле находится N натуральных чисел, записанных через пробел. 
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. 
# Найдите это число.

with open('file.txt', 'r') as data:
    text = data.read().split()
print(text)
text = list(map(int, text))
print(text)
text = [text[x]-1 for x in range(1, len(text)) if text[x] - 1 != text[x-1]]
print(text)
