def count_frequent_element(s: str) -> int:
    return max(map(lambda x: (s.count(x), x), s))[0]


def main():
    s = 'aaaaddddcccccccccc'
    print(count_frequent_element(s))


if __name__ == '__main__':
    main()
