# 1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).
# in
# 5
# out
# [10, 2, 3, 8, 9]
# 22

from random import sample
def random_num(count):
    if count<1:
        return 'Ошибка'
    else:
        random_elements = sample(range(1, count*3), count)
        return (random_elements)

def sum_num(new_list):
    size = len(new_list)
    sum_e = 0
    for i in range(0, size, 2):
        sum_e += new_list[i]
    return sum_e

my_list = random_num(int(input('Введите размер списка: ')))
print(my_list)
print(sum_num(my_list))