"""Создать словарь в качестве ключа которого будет 6-ти значное число (id), 
а в качестве значений кортеж состоящий из 2-х элементов - имя (str), возраст (int). 
Создать около 5-6 элементов словаря. Записать данный словарь на диск в json-файл."""

import json

users_data = {
    
    "123456": ("Jon", 25),
    "012345": ("Jim", 12),
    "987456": ("Liz", 32),
    "489612": ("Pam", 27),
    "746125": ("Tom", 5),
    "741025": ("Rick", 17)
}

with open("users.json", 'w') as write_users_to_file:
    json.dump(users_data, write_users_to_file)
    
    
