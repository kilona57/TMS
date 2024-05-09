"""Есть три целочисленные переменные, нужно
посчитать:
● сумму
● разность
● произведение
● от первой переменной отнять вторую и прибавить третью
● поделить произведение двух переменных на третью
● от суммы первых двух переменных найти остаток от
деления на третью переменную"""

number_one = 5
number_two = 15
number_three = -8

summ = number_one + number_two + number_three
difference = number_two - number_three - number_one
composition = number_one * number_two * number_three

res_one = number_one - number_two + number_three
res_two = (number_one * number_two) / number_three
res_three = (number_one + number_two) % number_three

print(summ, difference, composition, res_one, res_two, res_three, sep = '\n')