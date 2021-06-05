import heapq
from operator import mul
from functools import reduce


def get_calculate(number_list):
    smallest = heapq.nsmallest(3, number_list)
    biggest = heapq.nlargest(3, number_list)
    if reduce(mul, smallest, 1) > reduce(mul, biggest, 1):
        return sorted(smallest)
    else:
        return sorted(biggest)


with open('input.txt') as file:
    number_list = list(map(int, file.read().split()))

with open('output.txt', 'w') as file:
    file.write(' '.join(map(str, get_calculate(number_list))))
