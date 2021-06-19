from collections import Counter
from itertools import permutations


def calculate_variants(n, k, x):
    result = 0
    cnt = Counter(x)
    zipped_x = list(set(x))
    zipped_x.sort()
    end_set = set()
    for position, element in enumerate(zipped_x):
        high_border = element*k
        inner_cnt = Counter()
        inner_position = position
        while True:
            if inner_position == len(zipped_x):
                break
            if zipped_x[inner_position] <= high_border:
                if cnt[zipped_x[inner_position]] > 2:
                    result += 1
                    cnt[zipped_x[inner_position]] = 2
                inner_cnt[zipped_x[inner_position]
                          ] = cnt[zipped_x[inner_position]]

                inner_position += 1
            else:
                break
        if len(inner_cnt) < 2:
            continue
        inner_list = []
        for element in inner_cnt:
            inner_list.extend([element]*inner_cnt[element])
        if len(inner_list) < 3:
            continue

        end_set |= set(permutations(inner_list, 3))
    result += len(end_set)
    return result


with open('input.txt') as file:
    lines = file.readlines()
    n, k = tuple(map(int, lines[0].split()))
    x = list(map(int, lines[1].split()))


with open('output.txt', 'w') as file:
    file.write(str(calculate_variants(n, k, x)))
