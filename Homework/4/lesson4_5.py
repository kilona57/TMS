""" Сделать функцию принимающую кортеж строк и строку. 
Функция должна возвращать True если переданная строка имеется в переданном списке иначе False"""

def presence_string(tuple_string, string):
    if string in tuple_string:
        return True
    else:
        return False
print(presence_string(('Hello', 'Bye', 'Ilona', 'Ostis,', 'Sveta'), 'bye')) 
