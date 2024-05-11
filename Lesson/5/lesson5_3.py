numbers = ''
for num in range(1, 21):
    numbers += str(num) + ','
print(numbers[:-1])

numbers = ''
for num in range(2, 21, 2):
    numbers += str(num) + ','
print(numbers[:-1])

numbers = ''
for num in range(1, 21, 2):
    numbers += str(num) + ','
print(numbers[:-1])

words = ''
for num in range(1, 21):
    if num % 3 == 0:
        words += 'baz,'
    elif num % 5 == 0:
        words += 'bar, '
    else:
        words += str(num) + ','
print(words[:-1])

