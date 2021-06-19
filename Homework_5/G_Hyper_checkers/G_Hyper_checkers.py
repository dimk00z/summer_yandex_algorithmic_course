from collections import Counter
from itertools import permutations


def calculate_variants(n, k, x):
    result = 0
    cnt = Counter(x)
    # print(cnt)
    # previous_element = None
    for element in cnt:
        if cnt[element] > 2:
            result += 1
            cnt[element] = 2
        high_border = element*k
        cnt_with_border = {
            element: element_sum
            for element, element_sum in cnt.items()
            if element <= high_border and element_sum != 0
        }
        inner_list = []
        for inner_element in cnt_with_border:
            if cnt_with_border[inner_element] > 2:
                result += 1
                cnt_with_border[inner_element] = 2
            inner_list += [inner_element]*cnt_with_border[inner_element]
        if len(inner_list) == 1:
            continue
        # print(inner_list)
        inner_set = set(permutations(inner_list, 3))
        result += len(inner_set)
        # for inner_element in cnt_with_border:
        #     if
        cnt[element] = 0
        # print(cnt_with_border)
        # previous_element = element
        # print(inner_set, len(inner_set))
    return result


with open('input.txt') as file:
    lines = file.readlines()
    n, k = tuple(map(int, lines[0].split()))
    x = list(map(int, lines[1].split()))
    x.sort()


with open('output.txt', 'w') as file:
    file.write(str(calculate_variants(n, k, x)))
