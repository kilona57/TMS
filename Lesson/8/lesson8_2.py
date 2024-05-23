import os 
from typing import NoReturn

def create_folders(folder_path: str) -> NoReturn:
    
    while True:
        
        try:
            os.mkdir(folder_path)
            print(f"Папка '{folder_path}' успешно создана.")
            
        except FileExistsError:
            folder_path = input(f"Папка '{folder_path}' уже существует. Введите новое имя папки:  ")
        
        else:
            break

def create_file(folder_path: str, file_name: str) -> NoReturn:
    
    while True:
        
        file_path = os.path.join(folder_path, file_name)
        
        try:
            with open(file_path, 'x') as file:
                print(f"Файл '{file_name}' успешно создан в папке '{folder_path}'.")
        
        except FileExistsError:
            new_file_name = input(f"Файл '{file_name}' уже существует в папке '{folder_path}'.\\
                Введите новое имя файла: ")
            create_file(folder_path, new_file_name)

        
        except OSError:
            folder_path = input(f"Файл '{file_name}' не удалось создать в папке '{folder_path}'.\\
                Введите другое имя папки: ")
        
        else:
            break

def write_to_file(folder_path: str, file_name: str, data: str) -> NoReturn:
    
    file_path = os.path.join(folder_path, file_name)
    
    if not os.path.exists(folder_path):
        new_folder_path = input(f"Папка '{folder_path}' не найдена, не возможно записать данные в файл '{file_name}'.\\
            Введите другое имя папки: ")
        write_to_file(new_folder_path, file_name, data)
        return
        
        
    if not os.path.exists(file_path):
        new_file_name = input(f"Файл '{file_name}' в папке '{folder_path}' не найден, не возможно записать данные.\\
            Введите другое другое имя файла: ")
        write_to_file(folder_path, new_file_name, data)
        return
    
    while True:
                
        try:
            with open(file_path, 'a') as file:
                file.write(data)
                print(f"Данные успешно записаны в файл '{file_name}' в папке '{folder_path}'.")
        
        except OSError:
            print(f"Не удалось записать данные в файл '{file_name}' в папке '{folder_path}'.")
        
        else:
            break

def read_file(folder_path: str, file_name: str) -> NoReturn:
    
    file_path = os.path.join(folder_path, file_name)
    
    if not os.path.exists(folder_path):
        new_folder_path = input(f"Папка '{folder_path}' не найдена. Введите другое имя папки: ")
        read_file(new_folder_path, file_name)
        return
    
    if not os.path.exists(file_path):
        new_file_name = input(f"Файл '{file_name}' в папке '{folder_path}' не найден. Введите другое имя файла: ")
        read_file(folder_path, new_file_name)
        return
    
    while True:
        
        try:
            with open(file_path, 'r') as file:
                content = file.read()
                print(f"Содержимое файла '{file_name}' в папке '{folder_path}': \n{content}")
        
        except OSError:
            print(f"Не удалось прочитать файл '{file_name}' в папке '{folder_path}'.")
        else:
            break

create_folders("my_folder")
create_file("my_folder", "my_file.txt")
read_file("my_folder", "my_file.txt")
write_to_file("my_folder", "my_file.txt", 'Hello world!')
read_file("my_folder", "my_file.txt")