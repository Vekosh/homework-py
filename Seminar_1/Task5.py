# 5 Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D
# пространстве.
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21
from math import sqrt
x1 = int(input('x1 = '))
y1 = int(input('y1 = '))
x2 = int(input('x2 = '))
y2 = int(input('y2 = '))
distance = float(sqrt((x2-x1)*(x2-x1)+(y2-y1)*(y2-y1)))
print(round(distance, 2))
