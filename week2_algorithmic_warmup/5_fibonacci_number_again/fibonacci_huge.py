# Uses python3
import sys


def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n
    i = 1
    f1 = 0
    f2 = 1
    fn = f1 + f2
    sequence = [f1, f2]
    while i < n:
        fn = (f1 + f2) % m
        fn_old = fn
        f2_old = f2
        f2 = fn_old
        f1 = f2_old
        i += 1
        sequence.append(fn)
        if (i + 1) % 2 == 0:
            # check if we have gone through two periods:
            index = int((i+1) / 2)
            if sequence[0:index] == sequence[index:]:
                break
        if i == n:
            return fn
    # length of sequence
    length = int(len(sequence) / 2)
    index = int(n % length)
    value = sequence[index]
    return value

if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(get_fibonacci_huge_naive(n, m))
    sequence = get_fibonacci_huge_naive(n, m)
