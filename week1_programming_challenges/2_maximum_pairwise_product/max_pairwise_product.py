## python3
#
#
#def max_pairwise_product(numbers):
#    n = len(numbers)
#    max_product = 0
#    for first in range(n):
#        for second in range(first + 1, n):
#            max_product = max(max_product,
#                numbers[first] * numbers[second])
#
#    return max_product
#
#
#if __name__ == '__main__':
#    input_n = int(input())
#    input_numbers = [int(x) for x in input().split()]
#    print(max_pairwise_product(input_numbers))


# python3


def max_pairwise_product(numbers):
    n = len(numbers)
    max_num = 0
    sec_max_num = 0
    for i in range(n):
        if numbers[i] > max_num:
            sec_max_num = max_num
            max_num = numbers[i]
        elif numbers[i] > sec_max_num:
            sec_max_num = numbers[i]
    max_product = max_num * sec_max_num
    return max_product


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
