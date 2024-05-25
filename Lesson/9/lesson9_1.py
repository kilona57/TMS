"""Ввести с клавиатуры 4 строки и сохранить в 4 разные переменные. 
Создать файл и записать в него 2 строки и закрыть файл. 
Затем открыть файл на редактирование и дописать оставшиеся 2 строки. 
В итоговом файле должны быть 4 строки, каждая из которых должна начаться с новой строки"""

user_data = [input() for _ in range(4)]

file = open('data.txt', 'w', encoding = "UTF-8")
file.write(f"{user_data[0]}\n{user_data[1]}\n")
file.close()
file = open('data.txt', 'a', encoding = "UTF-8")
file.write(f"{user_data[2]}\n{user_data[3]}\n")
file.close()