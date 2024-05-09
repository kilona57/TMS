"""Сделать функцию принимающую кортеж строк и строку. 
Функция должна возвращать True если переданная строка имеется в переданном списке 
или является хотя бы частью строки (substr) иначе False"""

def return_true(tuple_string, search_string):
    for string in tuple_string:
        if search_string in string:
            return True
    return False
print(return_true(('Hello', 'Bye', 'bye', 'Ostis,', 'Sveta'), 'ye')) 
