class UserStorage:
    def __init__(self):
        self._users = {}

    def add_user(self, name, id_num, age=None, surname=None):
        if id_num in self._users:
            raise ValueError(f"Пользователь с id {id_num} уже существует!")
        user = User(name, id_num, age, surname)
        self._users[id_num] = user
        return user

    def get_user(self, id_num):
        if id_num not in self._users:
            raise ValueError(f"Пользователь с id {id_num} не найден.")
        return self._users[id_num]

    def update_user_name(self, id_num, new_name):
        user = self.get_user(id_num)
        user.name = new_name

    def update_user_age(self, id_num, new_age):
        user = self.get_user(id_num)
        user.age = new_age

    def update_user_surname(self, id_num, new_surname):
        user = self.get_user(id_num)
        user.surname = new_surname

class User:
    def __init__(self, name, id_num, age=None, surname=None):
        self._name = name
        self._id_num = id_num
        self._age = age
        self._surname = surname

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def id_num(self):
        return self._id_num

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, new_age):
        self._age = new_age

    @property
    def surname(self):
        return self._surname

    @surname.setter
    def surname(self, new_surname):
        self._surname = new_surname


user_storage = UserStorage()

user1 = user_storage.add_user("John", 123, 30, "Doe")

while True:
    id_num = int(input("Введите ID пользователя: "))
    try:
        user = user_storage.get_user(id_num)
        break
    except ValueError as e:
        print(e)

print(f"Выбран пользователь: {user.name} {user.surname}, ID: {user.id_num}, Возраст: {user.age}")

name_update = input("Введите новое имя (или нажмите Enter для пропуска): ")
if name_update:
    user_storage.update_user_name(user.id_num, name_update)
    print(f"Имя пользователя обновлено на: {user.name}")

age_update = input("Введите новый возраст (или нажмите Enter для пропуска): ")
if age_update:
    user_storage.update_user_age(user.id_num, int(age_update))
    print(f"Возраст пользователя обновлен на: {user.age}")

surname_update = input("Введите новую фамилию (или нажмите Enter для пропуска): ")
if surname_update:
    user_storage.update_user_surname(user.id_num, surname_update)
    print(f"Фамилия пользователя обновлена на: {user.surname}")