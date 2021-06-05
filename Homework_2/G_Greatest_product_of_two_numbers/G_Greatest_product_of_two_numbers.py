import heapq
from operator import mul


def get_calculate(number_list):
    smallest = heapq.nsmallest(2, number_list)
    biggest = heapq.nlargest(2, number_list)
    if mul(*smallest) > mul(*biggest):
        return sorted(smallest)
    else:
        return sorted(biggest)


with open('input.txt') as file:
    number_list = list(map(int, file.read().split()))

with open('output.txt', 'w') as file:
    file.write(' '.join(map(str, get_calculate(number_list))))
