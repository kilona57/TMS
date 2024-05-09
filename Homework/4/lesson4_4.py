"""Дан список чисел. Посчитать сколько раз встречается каждое число. 
Использовать для подсчета функцию"""

def counting_occurrences(list_number):
    dictionary = {}
    for number in list_number:
        if number in dictionary:
            dictionary[number] += 1
        else:
            dictionary[number] = 1
    return dictionary
print(counting_occurrences([1, 2, 3, 4, 1, 2, 3, 4, 1, 1, 1, 2, 2, 3, 5]))  
