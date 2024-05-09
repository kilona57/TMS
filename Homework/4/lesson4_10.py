"""Написать функцию, которая принимает список пользователей (имеющуюся структуру данных [ {}, {}, .. ])
 и печатает в консоль словарь, где ключ имя пользователя а значение - список с гражданствами пользователя"""

users = [
    {
        'name': 'Victor',
        'age': 10,
        'is_working': True,
        'citizenship':['Russian', 'England']
    },
    {
        'name': 'Pavel',
        'age': 20,
        'is_working': False,
        'citizenship':['Belarusian']
    },
    {
        'name': 'Svetlana',
        'age': 20,
        'is_working': True,
        'citizenship':['Belarusian', 'Georgia']
    },
] 

def print_citizenship(users):
    dict_count = {}
    for dictionary in users:
        key = dictionary.get('name')
        values = dictionary.get('citizenship')
        dict_count[key] = values
    print(dict_count)
print_citizenship(users)