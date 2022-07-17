'''
по заданному номеру четверти показывает координаты точек
'''
chetvert = int(input('введите номер четверти'))
def func(a):
    if a<1 or a>4:
        print('введите от 1 до 4')
    elif a == 1:
        print('x>0 , y>0')
    elif a == 2:
        print('x<0 ,y>0')
    elif a == 3:
        print('x<0,y<0')
    elif a == 4:
        print('x>0 , y<0')
func(chetvert)