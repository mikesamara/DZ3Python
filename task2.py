# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь 
# в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
list = []
k = int (input('Введите резмер списка: '))
count = 0
for i in range(k):
    list.append(input())
    
print (list)
    
x = input('Веедите число для поиска в списке: ')
res = list[0]
for i in list:
    if i < x:
        res = i

print(res)

