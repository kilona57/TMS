"""Тестовые данные для 5 задачи:
строка ‘TEST-STR’:
● S
● T
● TEST-
● TEST-S
● TS-T
● ETSR
● RTS-TSET
● RSTE
● 8"""

str = 'TEST-STR'
one = str[-3]
two = str[-2]
three = str[0:5]
four = str[0:6]
five = str [0:9:2]
six = str[1:9:2]
seven = str[::-1]
eight = str[9:0:-2]
nine = len(str)
print(one, two, three, four, five, six, seven, eight, nine, sep = '\n')
