"""Написать функцию, которая принимает список пользователей (имеющуюся структуру данных [ {}, {}, .. ]) 
и печатает имена этих пользователей и возраст в консоль.
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

def print_name_age_users(users):
    for dictionary in users:
        name = dictionary.get('name')
        age = dictionary.get('age')
        print(name,age)
        
print_name_age_users(users)