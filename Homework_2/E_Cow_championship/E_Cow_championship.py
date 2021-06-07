'''
10
555 76 661 478 889 453 555 359 601 835
555 подходит вроде (на 7 позиции)

52
645 535 575 155 965 805 700 115 875 805 485 465 75 955 275 835 105 115 75 325 435 975 695 965 985 745 115 65 95 525 445 715 815 85 755 365 685 935 945 195 775 465 335 475 585 425 45

'''


def fetch_Vasya_position(champions_number, results):
    if champions_number < 3:
        return 0
    max_result = max(results)
    max_position = results.index(max_result)
    if ((champions_number-1)-max_position) < 2:
        return 0
    Vasya_result = None
    # print(results)
    for position, value in enumerate(results[max_position:]):
        # print(value)
        if (value % 10 == 5) and (max_position+position+1) < champions_number:

            if results[max_position+position] > results[max_position+position+1]:
                Vasya_result = value
                # print(str(Vasya_result) + '  !!')
                break
    if Vasya_result:
        results = sorted(results,  reverse=True)
        # print(results, len(results))
        return results.index(Vasya_result)+1
    return 0


with open('input.txt') as file:
    lines = file.readlines()
    champions_number = int(lines[0])
    results = list(map(int, lines[1].split()))

with open('output.txt', 'w') as file:
    file.write(str(fetch_Vasya_position(champions_number, results)))
