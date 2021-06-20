from itertools import permutations


def calculate_variants(n, k, x):
    result = 0
    zipped_x = set()
    cnt = {}
    for element in x:
        if element not in cnt:
            cnt[element] = 0
        cnt[element] += 1
        zipped_x.add(element)
    zipped_x = list(zipped_x)
    zipped_x.sort()
    x = zipped_x
    end_set = set()
    for position, element in enumerate(zipped_x):
        high_border = element*k
        inner_cnt = {}
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
        for inner_element in inner_cnt:

            inner_list.extend([inner_element]*inner_cnt[inner_element])
        if len(inner_list) < 3:
            continue
        inner_set = set(permutations(inner_list, 3))

        end_set |= inner_set
        # end_set |= set(permutations(inner_list, 3))
    result += len(end_set)
    return result


with open('input.txt') as file:
    lines = file.readlines()
    n, k = tuple(map(int, lines[0].split()))
    x = list(map(int, lines[1].split()))


with open('output.txt', 'w') as file:
    file.write(str(calculate_variants(n, k, x)))
