# * 4. Напишите программу, которая принимает на вход 2 числа. Задайте список из N элементов, 
# заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях(не индексах).
# Position one: 1
# Position two: 3
# Number of elements: 5
# -> [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
# -> 15

p1 = int(input('Введите первую позицию: ')) - 1
p2 = int(input('Введите вторую позицию: ')) - 1
number = int(input('Введите колличество элементов: '))
if p1 > (number * 2 + 1) or p2 > (number * 2 + 1):
    print('Error input')
elif p1 < 0 or p2 < 0:
    print('Error input')
else:
    list_numbers = []
    for i in range(-number, number + 1):
        list_numbers.append(i)
    print(f'-> {list_numbers}')
    res = list_numbers[p1] * list_numbers[p2]
    print(res)