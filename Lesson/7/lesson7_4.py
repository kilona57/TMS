"""Сделать функцию декоратор, которая перед выполнением основной функции, выводит в консоль надпись ‘3.. 2.. 1.. 
Поехали’ и после выполнения функции выводит в консоль надпись ‘Стоп машина!’"""

def get_object(*args):
    result = []
    for i in args:
        a = i, str(type(i))
        result.append(a)
    print(result)

def dedcorator(func):
    print ('3.. 2.. 1.. Поехали')
    
    def object(*objects):
        func(*objects)
        print('Стоп машина!')
    return object

is_contain = dedcorator(get_object)
is_contain('25', [25,35,45])


    

