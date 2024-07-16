class User:
    _users = {}

    def __init__(self, name, id_num, age = None, surname = None):
        if id_num in User._users:
            raise ValueError(f"Пользователь с id {id_num} уже существует!")

        self._name = name
        self._id_num = id_num
        self._age = age
        self._surname = surname

        User._users[id_num] = self

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, args):
        new_name, id_num = args
        
        if id_num == self._id_num:
            self._name = new_name
        else:
            raise ValueError("Неверный id!")

    @property
    def id_num(self):
        return self._id_num

    @property
    def age(self, id_num):
        if id_num == self._id_num:
            return self._age
        else:
            raise ValueError("Неверный id!")
    
    @age.setter
    def age(self, args):
        new_age, id_num = args
        
        if id_num == self._id_num:
            self._age = new_age
        else:
            raise ValueError("Неверный id!")

    @property
    def surname(self, id_num):
        if id_num == self._id_num:
            return self._surname
        else:
            raise ValueError("Неверный id!")

    @surname.setter
    def surname(self, args):
        new_surname, id_num = args
        
        if id_num == self._id_num:
            self._new_surname = new_surname
        else:
            raise ValueError("Неверный id!")
