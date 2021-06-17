from collections import Counter


def get_coordinates(n, k, number_list):
    number_counter = Counter()
    left = 0
    result = (0,  len(number_list))

    for right, color in enumerate(number_list):
        number_counter[color] += 1
        if len(number_counter) == k:
            while number_counter[number_list[left]] > 1:
                number_counter[number_list[left]] -= 1
                left += 1

            if right - left < result[1] - result[0]:
                result = (left, right)
    return f'{result[0]+1} {result[1]+1}'


with open('input.txt') as file:
    lines = file.readlines()
    n, k = map(int, lines[0].split())
    number_list = [int(distance) for distance in lines[1].split()]


with open('output.txt', 'w') as file:
    file.write(str(get_coordinates(n, k, number_list)))
