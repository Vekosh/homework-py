# 2) Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
def find_num(x):
    my_list = []
    d = 2
    while x > 1:
        if x % d == 0:
            my_list.append(d)
            x //= d
        else:
            d +=1
    return my_list

print(find_num(int(input('Enter a natural number: '))))