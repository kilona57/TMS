def get_users_info():
    users_gender = ['мж', 'жен']
    gender = None
    
    while gender not in users_gender:
        print('Введите пол: муж или жен')
        gender = input().lower()
        name = input('Введите имя: ')
        age = input('Введите возраст: ')
        return gender, name, age
users_info = get_users_info()
print(users_info)