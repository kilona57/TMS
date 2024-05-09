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
    for dictionary in users:
        if dictionary['age'] >= 18:
            name = dictionary.get('name')
            age = dictionary.get('age')
            print(name,age)
print_name_age_more_eighteen(users)