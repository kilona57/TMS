"""Дан словарь, создать новый словарь, поменяв местами
ключ и значениею"""

def change_places(dictionary):
    new_dictionary = {value: key for key,value in dictionary.items()}
    return new_dictionary

print(change_places({1: 1.0, 2: 2.0, 3: 3.0}))