'''
Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N. Факториал
5! = 120
'''
n = int(input('введите число n '))
sum = 1
for i in range(2,n+1):
    sum = sum * i
print(sum)