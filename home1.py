'''Напишите программу, которая принимает на вход цифру, обозначающую день недели,
и проверяет, является ли этот день выходным.
Пример:

- 6 -> да
- 7 -> да
- 1 -> нет
'''
day = int(input('введите цифру дня недели'))
def func(a):
    if (a > 7) or (a < 1):
        print('такого дня нет')
    elif(a<6):
        print('нет')
    else:
        print('да')
func(day)



