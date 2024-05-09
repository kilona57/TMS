"""Тестовые данные для 5 задачи:
строка ‘Hello’, должно быть:
● l
● l
● Hello
● Hel
● Hlo
● el
● olleH
● olH
● 5"""

str = 'Hello'
one = str[2]
two = str[-2]
three = str[0:5]
four = str[0:3]
five = str[0:5:2]
six = str[1:3]
seven = str[::-1]
eight = str[::-2]
nine = len(str)
print(one, two, three, four, five, six, seven, eight, nine, sep = '\n')
