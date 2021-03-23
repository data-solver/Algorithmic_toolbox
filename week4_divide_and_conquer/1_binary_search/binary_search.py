# Uses python3
import sys
import math


def binary_search(a, x):
    left, right = 0, len(a)-1
    # write your code here
    while True:
        if left > right:
            return -1
        ind = math.floor((left + right) / 2)
        value = a[ind]
#        print(value)
        if x == value:
            return ind
        elif value > x:
            right = ind - 1
        elif value < x:
            left = ind + 1


def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

if __name__ == '__main__':
    input1 = sys.stdin.read()
    data = list(map(int, input1.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
#        print(linear_search(a, x), end = ' ')
        print(binary_search(a, x), end = ' ')
