def count_frequent_element(string: str) -> int:
    return max(map(
        lambda letter: (string.count(letter), letter),
        string))[0]


def main():
    s = 'aaaaddddcccccccccc'
    print(count_frequent_element(s))


if __name__ == '__main__':
    main()
