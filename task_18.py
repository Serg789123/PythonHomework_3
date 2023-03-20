# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
#     5
#     1 2 3 4 5
#     6
#     -> 5

import random
N = int(input("Введите количество элементов: "))
count = 0
A = [random.randint(0, 10) for item in range(N)]
print(A)
A.sort()
X = int(input("Введите сравниваемое число: ")) 
min = abs(X - A[0])
for i in range(len(A)-1):
    if A[i] == X:
        print(A[i]) 
        break 
    elif min >= abs(X - A[i+1]):
        min = abs(X - A[i+1])
        count +=1
print(A[count])
