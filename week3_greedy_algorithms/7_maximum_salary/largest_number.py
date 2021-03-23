#Uses python3

import sys
"""
idea: 
    sort all numbers by first digit 
        within each category, sort by 2nd digit

        12
        24
        53
        989
        473
        213
        4566
        3
        9
        h
        998
"""
#def is_greater(number, max_num):
#    n1 = len(str(number))
#    n2 = len(str(max_num))
#
#    if n1 >= n2:
#        n = n1
#        power = n - n2
#        max_num = max_num * 10 ** power
#    else:
#        n = n2
#        power = n - n1
#        number = number * 10 ** power
#    return number > max_num

def is_greater(number, max_num):
    num1 = int(str(number) + str(max_num))
    num2 = int(str(max_num) + str(number))
    return num1 > num2

def largest_number(a):
    #write your code here
    result = ""  
    while len(a) > 0:
        max_num = 0
        for number in a:
            if is_greater(number, max_num):
                max_num = number
        result = result + str(max_num)
        a.remove(max_num)
    return result

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
    
