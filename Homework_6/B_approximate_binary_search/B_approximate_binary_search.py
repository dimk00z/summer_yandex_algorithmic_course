def closest(lst, required_item):
    low = min(lst)
    high = max(lst)
    low_difference = abs(required_item-low)
    high_difference = abs(required_item-high)

    if low_difference == high_difference:
        return low
    return low if low_difference < high_difference else high


def approximate_binary_search(ordered_list,
                              required_item: int):
    low_value: int = 0
    high_value: int = len(ordered_list)-1
    result = None
    if required_item > ordered_list[-1]:
        return str(ordered_list[-1])
    if required_item < ordered_list[0]:
        return str(ordered_list[0])
    while low_value <= high_value:
        middle_value = (low_value+high_value)//2
        if required_item == ordered_list[middle_value]:
            result = required_item
            break
        if required_item > ordered_list[middle_value]:
            low_value = middle_value+1
        else:
            high_value = middle_value-1
    if not result:
        result = closest([ordered_list[low_value],
                         ordered_list[high_value]], required_item)
    return str(result)


def simple_check(first_list, second_list):
    checked = {}
    result = []
    for number in second_list:
        if number in checked:
            result.append(checked[number])
            continue
        checked[number] = approximate_binary_search(first_list,
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
