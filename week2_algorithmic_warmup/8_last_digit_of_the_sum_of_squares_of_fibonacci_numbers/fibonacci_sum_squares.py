# Uses python3
from sys import stdin


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


def fibonacci_sum_squares(n):
    val1 = get_fibonacci_huge_naive(n, 10)
    val2 = get_fibonacci_huge_naive(n+1, 10)
    result = (val1 * val2) % 10
    return result


def fibonacci_sum_squares_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current * current

    return sum % 10

if __name__ == '__main__':
    n = int(stdin.read())
    # n = 1234567890
    # print(fibonacci_sum_squares_naive(n))
    print(fibonacci_sum_squares(n))
