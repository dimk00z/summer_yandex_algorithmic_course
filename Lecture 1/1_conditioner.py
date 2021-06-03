
def air_condition(troom, tcond, mode) -> int:
    if mode == 'fan':
        return troom
    elif mode == 'auto':
        return tcond
    elif mode == 'heat':
        return troom if troom > tcond else tcond
    elif mode == 'freeze':
        return troom if tcond > troom else tcond


def main():
    troom, tcond = list(map(int, input().split()))
    mode = input()
    print(air_condition(troom, tcond, mode))
    # print(air_condition(10, 20, 'heat'))
    # print(air_condition(10, 20, 'freeze'))
    # print(air_condition(10, 20, 'auto'))
    # print(air_condition(10, 20, 'fan'))


if __name__ == '__main__':
    main()
