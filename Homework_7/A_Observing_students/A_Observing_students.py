from functools import reduce


def combine_overlaps(ranges):
    # https://coderoad.ru/15273693/Объединение-нескольких-диапазонов#59401068

    return reduce(
        lambda acc, el: acc[:-1:] + [(min(*acc[-1], *el), max(*acc[-1], *el))]
        if acc[-1][1] >= el[0] - 1
        else acc + [el],
        ranges[1::],
        ranges[0:1],
    )


def do_observing(n, m, b_e):

    result = 0
    result_intersection = combine_overlaps(sorted(b_e))
    for intersection in result_intersection:
        if intersection[1] == intersection[0]:
            result += 1
        else:
            result += intersection[1]-intersection[0]+1
    result = n - result
    # print(result_intersection, result)

    return str(result)


with open('input.txt') as file:
    lines = file.readlines()
    # n -students, m - teachers
    n, m = map(int, lines[0].split())
    # b_e - teachers
    b_e = [tuple(map(int, line.split())) for line in lines[1:]]


with open('output.txt', 'w') as file:
    file.write(do_observing(n, m, b_e))
