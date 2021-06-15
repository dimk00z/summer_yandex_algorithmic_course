from collections import Counter


def get_substring_length(
        string_length, substring_length, current_string):
    counter = Counter()

    left, right, sub_right, sub_left = 0, 0, 0, 0
    while right < string_length:
        if counter[current_string[right]] < substring_length:
            if (right-left) > (sub_right - sub_left):
                sub_right, sub_left = right, left
            counter[current_string[right]] += 1
            right += 1
        else:
            left = right-substring_length+1
            counter = Counter()

    return f'{sub_right-sub_left+1} {sub_left+1}'


with open('input.txt') as file:
    lines = file.readlines()
    string_length, substring_length = map(int, lines[0].split())
    current_string = lines[1].strip()

with open('output.txt', 'w') as file:
    file.write(get_substring_length(
        string_length, substring_length, current_string))
