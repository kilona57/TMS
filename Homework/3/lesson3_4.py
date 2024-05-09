"""Дана строка. Замените в этой строке все появления
буквы h на букву H, кроме первого и последнего вхождения."""

str = 'hhhhdfppdjhhhdkdhhdxlkh'
print(str.replace('h', 'H', str.count('h')-1).replace('H','h',1))
