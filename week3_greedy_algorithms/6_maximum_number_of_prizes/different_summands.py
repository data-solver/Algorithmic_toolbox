# Uses python3
import sys

def optimal_summands(n):
    summands = []
    total = 0
    i = 0
    while True:
        i += 1
        total += i
        if total + i + 1 <= n:
            summands.append(i)
        else:
            summands.append(n - total + i)
            break
    return summands


if __name__ == '__main__':
    input1 = sys.stdin.read()
    n = int(input1)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')