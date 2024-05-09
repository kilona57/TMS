"""Изменить функцию, так, что бы функция принимала вторым параметром возраст для проверки"""

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

def print_name_age_more_params(users, age):
    for dictionary in users:
        if dictionary['age'] >= age:
            name = dictionary.get('name')
            age_users = dictionary.get('age')
            print(name,age_users)
print_name_age_more_params(users, 9)