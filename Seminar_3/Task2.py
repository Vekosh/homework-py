# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# in
# 4
# out
# [2, 5, 8, 10]
# [20, 40]

from random import sample

def random_num(count):
    if count<1:
        return 'Ошибка'
    else:
        random_elements = sample(range(1, count*3), count)
        return (random_elements)

def product_pairs_num(new_list):
    res = 0
    length = len(new_list)
    res_list = []
    for i in range(length//2):
        res = new_list[i] * new_list[length - i - 1]
        res_list.append(res)
    if length % 2:
        res_list.append(new_list[length//2])
    return res_list

my_list = random_num(int(input('Введите длину списка: ')))
print(my_list)
if my_list != 'Ошибка':
    print(product_pairs_num(my_list))
else:
    print('List creation error')