# Задайте список из произвольных вещественных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# in
# 5
# out
# [5.16, 8.62, 6.57, 7.92, 9.22]
# Min: 0.16, Max: 0.92. Difference: 0.76


from random import uniform



def list_float(count):
    if count < 1:
        return 'Error'
    list_elements = []
    for i in range(count):
        list_elements.append(round(uniform(1, 10), 2))
    return list_elements


def min_max_num(new_list):
    length = len(new_list)
    min_num = new_list[0] % 1
    max_num = new_list[0] % 1
    for i in range(1, length):
        if min_num > new_list[i] % 1:
            min_num = round((new_list[i] % 1), 2)
        elif max_num < new_list[i] % 1:
            max_num = round((new_list[i] % 1), 2)

    res = round(max_num - min_num, 2)
    print(f'Min: {min_num}, Max:{max_num}. Difference: {res}')
    return res

list_1 = list_float(int(input('Введите размер списка: ')))
print(list_1)

print(min_max_num(list_1))

