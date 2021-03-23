# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0.
    # write your code here
    val_per_weight = [[values[i] / weights[i], weights[i]] for i in 
                      range(len(values))]
    val_per_weight.sort(reverse=True)
    for ratio, weight in val_per_weight:
        if weight >= capacity:
            value = value + ratio * capacity
            break
        else:
            value = value + ratio * weight
            capacity = capacity - weight
    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
#    n = 1
#    capacity = 10
#    values = [500]
#    weights = [30]
    
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
