# Задача: Дана последовательность 123456789101112..., 
# в которой выписаны подряд все натуральные числа и дано натуральное число k. 
# Написать программу, которая выводит k-ю цифру указанной последовательности (для больших k)
import datetime
import math
import threading

array = 1234567891011121314161617181920212223242526272829
def get_number(array:int , k:int) -> int:
    return int(str(array)[k-1])

print(get_number(array , 19))

# Стоун Семнадцатый, [10.07.2023 12:05]
# написать программу, которая будет возвращать последнюю цифру факториала не равную нулю

# программа должна работать при очень больших значениях

# Карина, [10.07.2023 12:17]
# То есть если ввести 6,то на выход получим 2, так как 6! =720, и не равная 0 последняя цифра - 2

def lost_number_of_factor(number:int):
    fact = 1
    for num in range(1,number+1):
        fact *=num
    str_fact = str(fact)    
    for ind in range(1, len(str_fact)):
        if str_fact[-ind:] !='0':
            return str_fact[-ind:]
    return None

print(lost_number_of_factor(30)) 
#print(5 * 10 ** 9 * (5 * 10 ** 9 - 1) * (5 * 10 ** 9 - 2)* (5 * 10 ** 9 - 3)* (5 * 10 ** 9 - 4)* (5 * 10 ** 9 - 5)* (5 * 10 ** 9 - 6)* (5 * 10 ** 9 - 7))

run = datetime.datetime.now()
print(run)
for i in range(1,5 * 10 ** 9):
    print(i)
end = datetime.datetime.now()
print(end)
# время работы кода неопределено(((((
