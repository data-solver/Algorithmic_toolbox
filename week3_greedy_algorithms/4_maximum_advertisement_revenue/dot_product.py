#Uses python3

import sys

def max_dot_product(a, b):
    #write your code here
    a.sort()
    b.sort()
    result = sum([a[i] * b[i] for i in range(len(a))])
#    res = 0
#    for i in range(len(a)):
#        res += a[i] * b[i]
    return result

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]
#    a = [1,3,-5]
#    b = [-2,4,1]
    print(max_dot_product(a, b))
    
