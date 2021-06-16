def binary_search(ordered_list,
                  required_item: int):
    step: int = 0
    low_value: int = 0
    high_value: int = len(ordered_list)-1
    while low_value <= high_value:
        step += 1
        middle_value = (low_value+high_value)//2
        if required_item == ordered_list[middle_value]:
            return 'YES'
        if required_item > ordered_list[middle_value]:
            low_value = middle_value+1
        else:
            high_value = middle_value-1
    return 'NO'


def simple_check(first_list, second_list):
    checked = {}
    result = []
    for number in second_list:
        if number in checked:
            result.append(checked[number])
            continue
        checked[number] = binary_search(first_list,
                                        number)
        result.append(checked[number])
    return '\n'.join(result)


with open('input.txt') as file:
    lines = file.readlines()
    n, k = map(int, lines[0].split())
    first_list = sorted([int(number) for number in lines[1].split()])
    second_list = [int(number) for number in lines[2].split()]


with open('output.txt', 'w') as file:
    file.write(simple_check(first_list, second_list))
