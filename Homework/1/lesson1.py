# while True:   
#     number = input('Please, enter a number(number of seconds): ', )
#     data = int(number)
#     days = data//86400
#     hours = ((data - (days*86400))//3600)
#     minutes = ((data - (hours*3600))-(days*86400)) // 60
#     seconds = (data%86400) % 60
#     res = ((days*86400)+(hours*3600)+(minutes*60)+seconds)
#     assert data == res
#     print('In', data, 'seconds:', days,'days,', hours,'hours,', minutes,'minutes,', seconds,'seconds.')


# a = [1,2,3]
# b = a
# print(a)
# print(b)
# c = [4,5,6]
# print(c)
# a = a + c
# print(a)
# print(b)

# a=[1]
# b=a
# print(a)
# print(b)
# a.append(12)
# print(a)
# print(b)

# nums = [0,1,2,3,4,5]
# print(nums)
# print (len(nums))
# nums.append (nums[:])
# print(nums)
# print(len(nums))

# lst=[0,1,2]
# print(lst.reverse())

# while True:   
#     number = input('Please, enter a number(number of seconds): ', )
#     data = int(number)
#     days = data//86164
#     hours = ((data - (days*86164))//3600)
#     minutes = ((data - (hours*3600))-(days*86164)) // 60
#     seconds = (data%86164) % 60
#     res = ((days*86164)+(hours*3600)+(minutes*60)+seconds)
#     assert data == res
#     print('In', data, 'seconds:', days,'days,', hours,'hours,', minutes,'minutes,', seconds,'seconds.')

# a,b = (int(input()) for i in ('месяц', 'день'))
# d = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
 
# if a not in d:
#     print(f'А месяцок то у вас не тот, введите число от 1 до 12 включительно')
# elif b not in range(1, d[a] + 1):
#     print(f'А денек то у вас не задался, введите число от 1 до {d[a]} включительно')
# else:
#     print(365 - sum(j for i, j in d.items() if i < a) - b)

# 1.int
# while True:
#     number_one = int(((str(int(True)))+(str(int(bool(None))))))
#     print('Number one =', number_one)
#     number_two = input('Please enter the number you want to add: ')
#     result = number_one + (int(number_two))
#     print('Number one + Number tow =', result,'\n')

# 2.float
# while True:
    # number_one = int(((str(int(True)))+(str(int(bool(None))))))
    # print('Number one =', number_one)
    # number_two = input('Please enter the number you want to add: ')
    # result = number_one + (float(number_two))
    # print('Number one + Number tow =', result)
    
# while True:
#     first_term = int(input('Please, enter first term: '))
#     second_term = float(input('Please, enter second term: '))
#     degree = int(input('Please, enter degree: '))
#     amount = ((first_term + second_term) ** degree)
#     print('Result=', amount)

# print(str(2+2)*int('2'+'2'))

# print(True + 2 + float(f'{int(bool("False"))}.5{int(True)}6'))

# number_one = 6
# number_two = 9
# id_num_one = str(id(number_one))
# id_num_two = str(id(number_two))
# sum = id_num_one + id_num_two
# difference = int(sum) - int(id_num_two)
# print(int(difference))


# def custom_summ(params):
#     return sum(params)

# summ_numbers = custom_summ([1,2,3])
# print(summ_numbers)

# a = [1,2,3]
# a.append(a)
# print(a)

# a = [1,2]
# b = sum(a)
# print(b)

# print(len([1,2,3]))
# print(len(10))

# names = ['Ivan','sveta','Pasha','Petr','Maria']

numbers = [1,2,6]
numbers.pop(0)
print(numbers)