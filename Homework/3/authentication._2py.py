"""* Создать 3 - 5 пользователей с именами и паролями имеющими сл. структуру:
users = [ (‘victor’, ‘password123’), (‘john’, ‘pass321’)]

Используя функции get_name, check_name, get_password, check_password и цикл сделать систему аутентификации, 
которая будет выдавать приветственное сообщение - Hey {name}! и выходить из цикла, 
в случае правильных введенных данных.
Выдавать сообщение об ошибке - Authentication Error. Check name or password! 
в случае неправильных введенных данных и запрашивать имя и пароль снова, 
пока пользователь не введет корректные данные."""

users =[('pasha', 'pas5365'), ('sveta', 'pass7965'), ('sonya', 'pasw1359'),\
    ('peter', 'pass5658'), ('ilona', 'passw8105')]

def get_name():
    return input('Введите имя пользователя: ')

def check_name(name):
    for items in users:
        if items[0] == name:
            return True
    return False

def get_password():
    return input('Введите пароль пользователя: ')   

        
def chek_password(name, password):
    for items in users:
        if items[0] == name and items[1] == password:
            return True
    return False

while True:
    name = get_name()
    if check_name(name):
        password = get_password()
        if chek_password(name, password):
            print('Hey', name,'!')
            break
        else:
            print('Authentication Error. Check password!')
    else:
        print('Authentication Error. Check name')