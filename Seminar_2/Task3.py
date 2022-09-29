#3. Задайте список из n чисел, заполненный по формуле (1 + 1/n) ** n и выведите на экран их сумму.
#Для n = 6: [2, 2, 2, 2, 2, 3] -> 13

numbers = []
n = int(input('Write count numbers: '))
for i in range(1, n+1):
    numbers.append(round((1 + 1/i) ** i))

sum_numbers = 0
for i in range(n):
    sum_numbers += numbers[i]

print(f'n = {n}: {numbers} -> {sum_numbers}')

