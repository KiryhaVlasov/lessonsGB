'''
напишите программу,которая на вход принимает координаты двух точек и находит
расстояние между ними в 2d пространстве
'''
import math

print('введите координаты точки a')
a1 = int(input('x= '))
a2 = int(input('y= '))
print('введите координаты точки б')
b1 = int(input('x= '))
b2 = int(input('y= '))
result =math.sqrt((a1-b1)**2 + (a2-b2)**2)
print(round(result,2))