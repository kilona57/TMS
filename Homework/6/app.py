from getters import get_email, get_password
from validators import check_data

def app():
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

    while True:
        email = get_email()
        if email.lower() == 'exit':
            print('Программа завершена.')
            break
    
        password = get_password()
        result = check_data(email, password, users)
        print(result)
        
if __name__ == '__main__':
    app()