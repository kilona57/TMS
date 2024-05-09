"""Дано трехзначное число, найти сумму его цифр.
Например, дано 123 – сумма 6, дано 555, сумма 15"""

number = input('Введите число: ')
int_number = number
summ = (int(number[0]) + int(number[1]) +int(number[2]))
print(summ)