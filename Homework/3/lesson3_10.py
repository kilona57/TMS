"""Создать функцию, в которой определена одна переменная со значением False.
Используя: len, not, вышеуказанную переменную и 
любые функции преобразования типов (int, float, bool, str, list …) вернуть список с числами 0, 1, 10"""

def func():
    num = False
    res_1 = int(num)
    res_2 = int(not(num))
    res_3 = int(str(res_2) + str(res_1))
    res = [res_1, res_2, res_3]
    return res

fun_list = func()
print(fun_list)