users = [
     {
        'email': 'svet123a@mail.ru',
        'password': '123password'
    },
    {
        'email': 'perzovpavel@gmail.com',
        'password': 'perez6pass'
    },
    {
        'email': 'ribakovaira@yandex.ru',
        'password': 'tapochec265pass',
        'age': 12
    },
]

def get_mail():
    return input('Введите email: ')
    
def get_password():
    return input('Введите password: ')
  
def check_data(email, password):
    for user in users:
        if user['email'] == email and user['password'] == password:
            return user['email']
    return 'Ошибка: не верный email или password.'

while True:
    email = get_mail()
    if email == 'exit':
        print('Программа завершена.')
        break
    
    password = get_password()
    result = check_data(email, password)
    print(result)