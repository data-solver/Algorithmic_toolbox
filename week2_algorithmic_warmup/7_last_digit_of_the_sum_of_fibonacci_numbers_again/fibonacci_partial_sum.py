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


def fibonacci_sum_naive(n):
    value = get_fibonacci_huge_naive(n+2, 10)
    return (value - 1) % 10


def fibonacci_partial_sum(from_, to):
    sum1 = fibonacci_sum_naive(from_-1)
    sum2 = fibonacci_sum_naive(to)
    result = (sum2 - sum1) % 10
    return result


def fibonacci_partial_sum_naive(from_, to):
    sum = 0

    current = 0
    next = 1

    for i in range(to + 1):
        if i >= from_:
            sum += current

        current, next = next, current + next

    return sum % 10


if __name__ == '__main__':
    input = sys.stdin.read();
    from_, to = map(int, input.split())
    # from_ = 10
    # to = 200
    # print(fibonacci_partial_sum_naive(from_, to))
    print(fibonacci_partial_sum(from_, to))
