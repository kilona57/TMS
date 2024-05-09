# 1. Дз задание1 (int)
while True:
    number_one = int(((str(int(True)))+(str(int(bool(None))))))
    print('Number one =', number_one)
    number_two = input('Please enter the number you want to add: ')
    result = number_one + (int(number_two))
    print('Number one + Number tow =', result)

# 2. Дз задание1 (float)
while True:
    number_one = int(((str(int(True)))+(str(int(bool(None))))))
    print('Number one =', number_one)
    number_two = input('Please enter the number you want to add: ')
    result = number_one + (float(number_two))
    print('Number one + Number tow =', result)

# 3. Дз задание2
while True:
    first_term = int(input('Please, enter first term: '))
    second_term = float(input('Please, enter second term: '))
    degree = int(input('Please, enter degree: '))
    amount = ((first_term + second_term) ** degree)
    print('Result =', amount,'\n')

#4. Доп.задание 25слайд
number_one = 6
number_two = 9
id_num_one = str(id(number_one))
id_num_two = str(id(number_two))
sum = id_num_one + id_num_two
difference = int(sum) - int(id_num_two)
print(int(difference))

# 5. Прошлое дз(+hours, cутки = 86164с)
while True:   
    number = input('Please, enter a number(number of seconds): ', )
    data = int(number)
    days = data//86164
    hours = ((data - (days*86164))//3600)
    minutes = ((data - (hours*3600))-(days*86164)) // 60
    seconds = (data%86164) % 60
    res = ((days*86164)+(hours*3600)+(minutes*60)+seconds)
    assert data == res
    print('In', data, 'seconds:', days,'days,', hours,'hours,', minutes,'minutes,', seconds,'seconds.')