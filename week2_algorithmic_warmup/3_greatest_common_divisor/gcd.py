# Uses python3
import sys

def gcd_naive(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd

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
            

if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd(a, b))
