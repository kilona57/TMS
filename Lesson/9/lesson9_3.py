"""Прочитать сохраненный json-файл и записать данные на диск в csv-файл, 
первой строкой которого озаглавив каждый столбец и добавив новый столбец "телефон"."""

import json
import csv
import random 

with open('users.json') as read_users:
    users_data = json.load(read_users)

with open("users.csv", "w", newline="") as write_users_to_csv_file:
    writer = csv.writer(write_users_to_csv_file)
    writer.writerow(["ID", "Name", "Age", "Phone number"])

    for id, person in users_data.items():
        name, age = person
        phone = f"+375(29){random.randrange(0000000 , 9999999 , 1)}"
        writer.writerow([id, name, age, phone])