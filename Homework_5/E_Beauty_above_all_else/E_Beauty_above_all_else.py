from collections import Counter


def get_coordinates(n, k, number_list):
    number_counter = Counter(number_list)
    left = 0
    right = n-1
    while number_counter[number_list[left]] != 1:
        number_counter[number_list[left]] -= 1
        left += 1
    while number_counter[number_list[right]] != 1:
        number_counter[number_list[right]] -= 1
        right -= 1
    return f'{left+1} {right+1}'


with open('input.txt') as file:
    lines = file.readlines()
    n, k = map(int, lines[0].split())
    number_list = [int(distance) for distance in lines[1].split()]


with open('output.txt', 'w') as file:
    file.write(str(get_coordinates(n, k, number_list)))
