# Uses python3
import sys


def get_change(m):
    # write your code here
    count = 0
    denominations = [10, 5, 1]
    for val in denominations:
        while m >= val:
            count += 1
            m -= val

    return count


if __name__ == '__main__':
    m = int(sys.stdin.read())
    # m = 28
    print(get_change(m))
