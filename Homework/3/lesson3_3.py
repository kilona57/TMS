"""Дана строка, состоящая из слов, разделенных
пробелами. (Вот 4 варианта тестовых данных для программы:
‘Hello world’, ‘a b c’, ‘test’, ‘test1 test2 test3 test4 test5’).
Определите, сколько в ней слов."""

str = 'Hello word'
str_2 = 'a b c'
str_3 = 'test'
str_4 = 'test1 test2 test3 test4 test5'

words = str.split()
words_two = str_2.split()
words_three = str_3.split()
words_four = str_4.split()

print((len(words)), len(words_two), len(words_three), len(words_four), sep = '\n')
