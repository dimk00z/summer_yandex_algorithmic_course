def count_frequent_element(string: str) -> int:
    return max(map(
        lambda letter: (string.count(letter), letter),
        string))[0]


def count_frequent_element_with_set(string: str) -> dict:
    freq_letter = ''
    freq_letter_count = 0
    for current_letter in set(string):
        current_letter_count = 0
        for letter in string:
            if current_letter == letter:
                current_letter_count += 1
        if current_letter_count > freq_letter_count:
            freq_letter = current_letter
            freq_letter_count = current_letter_count
    return {freq_letter: freq_letter_count}


def count_frequent_element_with_dict(string: str) -> dict:
    dct = {}
    for current_letter in string:
        if current_letter in dct:
            dct[current_letter] += 1
        else:
            dct[current_letter] = 1
    frequent_element = max(dct, key=dct.get)
    return {frequent_element: dct[frequent_element]}


def main():
    s = 'aaaaddddcccccccccc'
    print(count_frequent_element(s))
    print(count_frequent_element_with_set(s))
    print(count_frequent_element_with_dict(s))


if __name__ == '__main__':
    main()
