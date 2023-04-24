list = []
k = int (input('Введите резмер списка: '))
x = input('Веедите число для поиска в списке: ')
count = 0
for i in range(k):
    list.append(input())
    if x == list[i]:
        count +=1
    
print(f'{count},  столько раз встречается данный {x} элемент в списке')