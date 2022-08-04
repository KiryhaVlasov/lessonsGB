'''
1.Вычислить число c заданной точностью d
Пример:
- при d = 3, π = 3.141


import math
d = int(input('задайте точность'))
a = math.sqrt((2-math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+(math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+1)))))))))))
p = (3 * 2**8) * a
print(round(p,d))
'''


'''
2.Задайте натуральное число N. Напишите программу, которая составит 
список простых делителей числа N. (1 - составное число)

n = int(input('введите натуральное число'))
for i in range(1,n+1):
     if n % i  == 0:
         print(i, end =' ')
'''
from random import randint
d = int(input('введите натуральную степень'))
a = randint(0,100)
b = randint (0,100)
c = randint(0,100)
print(a,'x^',d,'+',b,'x','+',c, end='')