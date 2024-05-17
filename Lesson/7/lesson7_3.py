"""С помощью map привести список словарей к сл. виду:
Каждый словарь содержит ключ email и значение - непосредственно сам адрес.
Привести все адреса к нижнему регистру.
"""

users = [
    {'email': 'KORASACOVASVETA@GMAIL.COM'},
    {'email': 'KONDRATIEVAILONA@MAIL.RU'},
    {'email': 'PERZOVPAVEL@GMAIL.COM'},
    {'email': 'RYBOKOVAIRINA@MAIL.RU'},
    {'email': 'MAKARENKOANNA@GMAIL.COM'}
]


print(list(map(lambda k: k.lower(),[item.get('email') for item in users])))

