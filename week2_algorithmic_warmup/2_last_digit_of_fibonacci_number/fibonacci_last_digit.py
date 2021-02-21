# Uses python3
import sys

def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n
    i = 1
    f1 = 0
    f2 = 1
    fn = f1 + f2
    while i < n:
        fn = (f1 + f2) % 10
        fn_old = fn
        f2_old = f2
        f2 = fn_old
        print(f"f1 ={f1}\n f2={f2}\n fn={fn}")
        f1 = f2_old
        i += 1
    return fn

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(get_fibonacci_last_digit_naive(n))

#print(get_fibonacci_last_digit_naive(10))
