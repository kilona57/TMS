"""Используя условные операторы, в модуле authentication.py 
создать функции check_password и get_password которая будет проверять и получать пароль пользователя 
соответственно get_name, check_name.
"""
def get_name():
    return input('Введите имя пользователя: ')

def check_name(name):
    if '@' in name:
        print('Верное имя пользователя!')
    else:
        print ('Проверти наличие @ в вашем имени!')
        
def get_password():
    return input('Введите пароль пользователя: ')

def chek_password(password): 
    if len(password) < 8:
        print('Проверить длину пароля, она должна быть больше 8')
    else:
        print ('Верный пароль!')
        
while True:
    name = get_name()
    password = get_password()
    ckeck_mame = check_name(name)
    ckeck_password = chek_password(password)

             
        
