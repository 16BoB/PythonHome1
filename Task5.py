# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

import math
	
first_dot_x = int(input('Введите координату х первой точки: '))
first_dot_y  = int(input('Введите координату y первой точки: '))
second_dot_x = int(input('Введите координату х второй точки: '))
second_dot_y = int(input('Введите координату y второй точки: '))
distance = math.sqrt( ((first_dot_x-second_dot_x)**2)+((first_dot_y-second_dot_y)**2) )
print(round(distance, 2))