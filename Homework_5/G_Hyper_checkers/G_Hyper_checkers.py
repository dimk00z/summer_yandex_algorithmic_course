from collections import Counter


def calculate_variants(n, k, x):
    result = 0
    cnt = Counter(n)
    for element, element_sum in cnt.items():
        if element_sum >= 3:
            result += 1
    return result


with open('input.txt') as file:
    lines = file.readlines()
    n, k = tuple(map(int, lines[0].split()))
    x = list(map(int, lines[1].split()))
    x.sort()


with open('output.txt', 'w') as file:
    file.write(str(calculate_variants(n, k, x)))
