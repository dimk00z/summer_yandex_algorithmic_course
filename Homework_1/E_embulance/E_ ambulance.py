def round_up(v, d):
    result = v // d + (1 if v % d else 0)
    return result


def get_P1_and_N1(room_1, max_level, room_old, p_old, level_old):
    count_room_for_level = 0
    if max_level == 1 and p_old == 1:
        return 1, 1

    for count_room_for_level in range(40):
        if ((level_old - 1) * count_room_for_level) *\
                p_old < room_old < (count_room_for_level * level_old) * p_old:
            break
    else:
        return -1

    p_new = round_up(room_1, (max_level * count_room_for_level))

    level_new = round_up(room_1, count_room_for_level) % max_level
    return p_new, level_new


with open('input.txt') as file:
    k1, m, k2, p2, n2 = map(int, file.read().split())


p1, n1 = get_P1_and_N1(k1, m, k2, p2, n2)

with open('output.txt', 'w') as file:
    file.write(f'{p1} {n1}')
