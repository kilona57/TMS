"""Написать функцию, которая принимает список пользователей (имеющуюся структуру данных [ {}, {}, .. ]) 
и добавляет пользователю данные статуса. Значение статуса устанавливать
- в suspicious, если пользователь младше 18 и работает или старше 18 и не работает..
- в not_suspicious, если пользователь младше 18 и не работает или старше 18 и работает.
Функция должна возвращать обновленный список с пользователями.
"""

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

def add_suspicious(users):
    for dictionary in users:
        age = dictionary.get('age')
        is_working = dictionary.get('is_working')
        if (age < 18 and is_working) or (age > 18 and not is_working):
            dictionary['status'] = 'suspicious'
        else:
            dictionary['status'] = 'not_suspicious' 
    print(users)
        
add_suspicious(users)