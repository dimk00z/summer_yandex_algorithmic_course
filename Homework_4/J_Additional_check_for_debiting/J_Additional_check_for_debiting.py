from collections import Counter
import re


def get_the_most_frequent_word(c, d, text, n):
    is_digit_first = True if d == 'yes' else False
    is_case_sensitive = True if c == 'yes' else False
    text_counter = Counter()
    key_words = set()

    if n:
        for line in text[:n]:
            line = line.strip()
            if len(line) > 50:
                continue
            key_words.add(
                line if is_case_sensitive else line.lower())
    start = 0 if not n else n
    for line in text[start:]:
        if not is_case_sensitive:
            line = line.lower()
        line = re.sub(r'[^a-zA-Z0-9_]', ' ', line)
        for word in line.split():
            if word in key_words:
                continue
            if word[0].isdigit():
                if not is_digit_first:
                    continue
                if is_digit_first and not (any(map(str.isalpha, word)) or "_" in word):
                    continue
            text_counter[word] += 1

    result = '' if not text_counter else text_counter.most_common(1)[0][0]
    return result


with open('input.txt') as file:
    lines = file.readlines()
    n, c, d = lines[0].split()
    n = int(n)
    text = [line.strip() for line in lines[1:]]


with open('output.txt', 'w') as file:
    file.write(str(get_the_most_frequent_word(c, d, text, n)))
