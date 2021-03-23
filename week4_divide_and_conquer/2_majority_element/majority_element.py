# Uses python3
import sys
import numpy as np

def get_majority_element(a, left, right):
    count = 0
    candidate = None

    for num in a:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)
    count = 0
    if candidate:
        for num in a:
            if num == candidate:
                count += 1
        n = len(a)
        if count > n/2:
            pass
        else:
            candidate = None
    return candidate
    
    #write your code here

def generate_test_majority_element(n):
    array_with_major = [1] * (n//2)+ [i for i in range(2, n//2 + 1)]
    array_without_major = [1] * (n//2) + [i for i in range(2, n//2 + 3)]
    try:
        assert get_majority_element(array_with_major, 0, n-1) == 1
    except AssertionError:
        print('failed')
        return array_with_major
    try:
        assert get_majority_element(array_without_major, 0, n+1 ) == -1
    except AssertionError:
        print('failed')
        return array_without_major
    return 0
#n_vals = np.arange(1e6, 2e6, 1e5)
#for n in n_vals:
#    n = int(n)
#    temp = generate_test_majority_element(n)
#    if temp != 0:
#        print(temp)
#        break

if __name__ == '__main__':  
    input1 = sys.stdin.read()
    n, *a = list(map(int, input1.split()))
    if get_majority_element(a, 0, n):
        print(1)
    else:
        print(0)
