from collections import Counter
import re


def get_the_most_frequent_word(c, d, text):
    is_digit_first = True if d == 'yes' else False
    is_case_sensitive = True if c == 'yes' else False
    text_counter = Counter()
    for line in text:
        if not is_case_sensitive:
            line = line.lower()
        line = re.sub(r'[^a-zA-Z0-9]', ' ', line)
        for word in line.split():
            if not is_digit_first:
                if word[0].isdigit():
                    continue
            text_counter[word] += 1
    return text_counter.most_common(1)[0][0]


with open('input.txt') as file:
    lines = file.readlines()
    n, c, d = lines[0].split()
    text = [line.strip() for line in lines[1:]]


with open('output.txt', 'w') as file:
    file.write(str(get_the_most_frequent_word(c, d, text)))
