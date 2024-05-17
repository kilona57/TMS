"""Создать функцию is_contain_baz которая принимает на вход строку, и отдает True 
если в этой строке есть подстрока baz иначе отдает False"""

def is_contain_baz(input_str):
    return 'baz' in input_str

"""Создать функцию is_contain_foo которая принимает на вход строку, и отдает True 
если в этой строке есть подстрока foo иначе отдает False"""
def is_contain_foo(input_str):
    return 'foo' in input_str

"""Создать функцию filter_strings которая принимает на вход итерируемый объект строк (list, tuple) и функцию. 
Внутри она должна вызывать входящую функцию и передавать туда каждую строку из входного списка. 
Отдавать должна список тех строк, которые прошли проверку входящей функцией.. 
Т. Е. Если мы передали на вход
список [‘lala’, ‘bahabaz’, ‘baza’, ‘haka’]
функцию is_contain_baz
То получить мы должны [‘bahabaz’, ‘baza’] Проверить что с is_contain_foo все работает подобным образом."""
def filter_strings(input_strings, func):
    filter_strings = []
    for string in input_strings:
        if func(string):
            filter_strings.append(string)
    return filter_strings

strings = ['lalala', 'labaz', 'baz', 'lafoo', 'foo']
filtered = filter_strings(strings, is_contain_foo)
print(filtered)