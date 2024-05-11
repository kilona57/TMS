"""Написать функцию, которая, используя цикл for in, запрашивает у пользователя его
имя, возраст и пол и возвращает эти данные в кортеже.
Важно сделать проверку на пол, так как у пользователя только два варианта. (муж жен) и
во избежания ошибок - предоставить эту выборку (муж жен) пользователю перед вводом."""
def get_user_info():   
    users_info = [('name', 'enter name: '), ('age', 'enter age: '), ('gender', 'enter gender (m/f): ')]
    user_data = {}
    for i in users_info:
        data = input(i[1])
        user_data[i[0]] = data
        if i[0] == 'gender' and (data == 'm' or data == 'f'):
            return user_data
    else: 
        print("Wrong gender")
print(get_user_info())
        

    
    