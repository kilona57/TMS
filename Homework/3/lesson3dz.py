
# # доп

# users_file = 'user.txt'

# def load_users():
#     try: 
#         with open(users_file, 'r') as file:
#             users_data = file.read()
#             if users_data:
#                 users = txt.loads()
#     except FileNotFoundError:
#         users = {}
#     return users
        
# def save_users(users):
#     with open (users_file, 'w') as file:
#         for name, password in users.items():
#             file.write(f'{name} : {password}\n')
    
# def register_users(users):
#     name = input('Введите имя пользователя: ')
#     password = input('Введите пароль пользователя: ')
    
#     users[name] = password
#     save_users(users)
#     print('Пользователь успешно зарегестрирован!')

# def authenticate_users(users):
#     name = input('Введите имя пользователя: ')
#     password = input('Введите пароль пользователя: ')
#     if users.get(name) == password:
#         return True
#     else:
#         return False
    
# def change_age():
#     age = input('Введите новый возраст: ')
#     print('Возраст успешно изменен!')

# def main():
#     users = load_users()
#     while True:
#         if not users:
#             print('Регестрация нового пользователя.')
#             register_users(users)
#         authenticated =False
#         while not authenticated:
#             print('Аунтификация пользователя.')
#             authenticated = authenticate_users(users)
#             if not authenticated:
#                 print('Направильное имя или пароль пользователя. Попробуйте снова.')
#         print('Вы успешна аунтифицированы.')
        
#         choice = input('Выбирите действие: [C]Изменить возраст, [Q]Выйти из системы: ').upper()
#         if choice == 'C':
#             change_age()
#         elif choice == 'Q':
#             print('Выход из ситсемы.')
#             break

# if __name__ == '__main__':
#     main()
        