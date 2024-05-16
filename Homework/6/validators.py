def check_data(email, password, users):
    for user in users:
        if user["email"] == email:
            if user["password"] == password:
                return email
            else:
                return "Ошибка: Неверный пароль."
    return "Ошибка: Пользователь с таким email не найден."