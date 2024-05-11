data = [(1,2,3), (4,5), (6,7,8), (9, 10)]
for tup in data:
    first_elements = tup[0]
    print(first_elements)
for tup in data:
    *last_elemnts, = tup[1:]
    print(last_elemnts)

