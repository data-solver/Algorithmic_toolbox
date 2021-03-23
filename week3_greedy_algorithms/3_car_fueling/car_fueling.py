# python3
import sys


def compute_min_refills(distance, tank, stops):
    n = len(stops)
    total = 0
    current = 0
    stops.append(distance)
    stops = [0.] + stops
    while current <= n:
        last = current
        while current <= n and stops[current+1] - stops[last] <= tank:
            current += 1
        if current == last:
            return -1
        if current <= n:
            total += 1
    return total


if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
#    d = 900
#    m = 200
#    stops = [100, 200, 300, 400]
    print(compute_min_refills(d, m, stops))
