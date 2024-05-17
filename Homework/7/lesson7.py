"""Используя built-in модуль time написать декоратор, который будет измерять время работы функции.
Он должен возвращать результат работы функции и время в кортеже, где единица измерения времени на свое усмотрение.
Для тестирования подойдет функция sleep из этого модуля, 
которая останавливает процесс выполнения программы на заданное количество секунд."""

import time 

def dedcorator(func):
    print ('3.. 2.. 1.. Поехали')
    def object(*objects):
        start_time = time.time()
        func(*objects)
        print('Стоп машина!')
        print("--- %s seconds ---" % (time.time() - start_time))
    return object

@dedcorator
def get_object(*args):
    time.sleep(3)
    result = []
    for i in args:
        a = i, str(type(i))
        result.append(a)
    print(result)
    
is_contain = get_object('25', [25,35,45])