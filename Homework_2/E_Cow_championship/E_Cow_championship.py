'''
10
555 76 661 478 889 453 555 359 601 835
555 подходит вроде (на 7 позиции)
'''


def fetch_Vasya_position(champions_number, results):
    if champions_number < 3:
        return 0
    max_result = max(results)
    max_position = results.index(max_result)
    if ((champions_number-1)-max_position) < 2:
        return 0
    for position, value in enumerate(results[max_position-1:]):
        if (value % 10 == 5) and (max_position+position+1) < champions_number:
            if results[max_position+position] < value:
                Vasya_result = value
                Vasya_position = position + max_position
                print(Vasya_result, Vasya_position)
    return 0
    # Vasya_position = max_position+1
    # Vasya_result = results[Vasya_position]
    # print(max_result, Vasya_result)
    # print(results)
    # if (Vasya_result % 10) != 5 or results[Vasya_position+1] > Vasya_result:
    #     return 0
    # results = sorted(results,  reverse=True)
    # print(results, len(results))
    # return results.index(Vasya_result)+1


with open('input.txt') as file:
    lines = file.readlines()
    champions_number = int(lines[0])
    results = list(map(int, lines[1].split()))

with open('output.txt', 'w') as file:
    file.write(str(fetch_Vasya_position(champions_number, results)))
