# numbers = ''
# for num in range(1, 21):
#     numbers += str(num) + ','
# print(numbers[:-1])

# numbers = ''
# for num in range(2, 21, 2):
#     numbers += str(num) + ','
# print(numbers[:-1])

# numbers = ''
# for num in range(1, 21, 2):
#     numbers += str(num) + ','
# print(numbers[:-1])

# words = ''
# for num in range(1, 21):
#     if num % 3 == 0:
#         words += 'baz,'
#     elif num % 5 == 0:
#         words += 'bar, '
#     else:
#         words += str(num) + ','
# print(words[:-1])

# data = [(1,2,3), (4,5), (6,7,8), (9, 10)]
# for tup in data:
#     first_elements = tup[0]
#     print(first_elements)
# for tup in data:
#     *last_elemnts, = tup[1:]
#     print(last_elemnts)

data = [(1,2,3), (4, 'hello'), ('string',7,'eight'), (9, 'bye')]

for tup in data:
    for elements in tup:
        print(elements, end = ',')