# Uses python3
import sys

def gcd(a, b):
    if a == b:
        return a
    a1 = max(a, b)
    b1 = min(a, b)
    while True:
        r = a1 % b1
        if r == 0:
            return b1
        a1 = b1
        b1 = r

def lcm(a, b):
    d = gcd(a, b)
    return int(a*b/d)

def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm(a, b))

