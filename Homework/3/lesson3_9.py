"""Дано трехзначное число, найти сумму его цифр.
Например, дано 123 – сумма 6, дано 555, сумма 15"""

number = input('Введите число: ')
int_number = int(number)
sot = (int_number // 100)
des = ((int_number // 10) % 10)
ed =  (int_number % 10)
summ = sot + des + ed
print(sot, des, ed, sum, sep = '\n')

