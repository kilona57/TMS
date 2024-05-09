"""Сделать функцию принимающую list строк, и параметр длины. 
Функция должна возвращать список строк, длина которых больше параметра длины"""

def string_larger(list_string, length):
    new_list = []
    for string in list_string:
        if len(string) > length:
            new_list.append(string)
    return new_list

print(string_larger(['Hello', 'My name Ilona', 'Ostis', 'septemper'],8 ))