data = [(1,2,3), (4, 'hello'), ('string',7,'eight'), (9, 'bye')]

for tup in data:
    for elements in tup:
        print(elements, end = ',')