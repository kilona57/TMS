"""Используя функцию isinstance, создать функцию которая принимает на вход объект любого типа, 
и возвращает строковый объект значение которого равно типу входного объекта.
Перечень допустимых объектов: tuple, string, dict, list
As an example:
>>> get_type(tuple())
‘Tuple’"""

def get_object(custom_obj):
    if isinstance(custom_obj,(tuple, str, dict, list)):
        return (str(type(custom_obj)))

print(get_object('25'))

"""Расширить функционал этой функции, сделав так, что бы функция могла принимать, 
сколь угодное количество объектов, и возвращать список кортежей, где первый элемент - сам объект, 
второй - така же строковый объект равный типу объекта
As an example:
>>> get_types(tuple(), [], {}, [1, ‘str’])
[(tuple(), ‘Tuple’), ([], ‘List’), ({}, ‘Dict’), ([1, ‘str’], ‘List’)]"""

def get_object(*args):
    result = []
    for i in args:
        a = i, str(type(i))
        result.append(a)
    return (result)

print(get_object('25', [25,35,45]))
