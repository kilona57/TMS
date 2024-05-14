"""Написать функцию, которая принимает список пользователей (имеющуюся структуру данных [ {}, {}, .. ]) 
и печатает имя и возраст в консоль тех пользователей, возраст которых больше либо равен 18 лет.
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

def print_name_age_more_eighteen(users):
    for user in users:
        if user['age'] >= 18:
            name = user.get('name')
            age = user.get('age')
            print(name,age)
print_name_age_more_eighteen(users)