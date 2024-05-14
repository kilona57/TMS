"""Дан словарь, создать новый словарь, поменяв местами
ключ и значениею"""

def change_places(dictionary):
    new_dictionary = {}
    for key, value in dictionary.items():
        try:
            if isinstance(value, (int, str, float)):
                new_dictionary[value] = key
            else:
                print(f'Значение{value} не является допустимым типом. Он пропускается')
        except TypeError:
            print(f'Значение{value} не является допустимым типом. Он пропускается')
    return new_dictionary

dictionary = {'one': 1, 2: 'two', 'three': [3,4], 'four': 4}
change_dictionary = change_places(dictionary)
print(change_dictionary)