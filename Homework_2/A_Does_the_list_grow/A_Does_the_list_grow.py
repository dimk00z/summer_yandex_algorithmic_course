def is_list_ascending(number_list):
    previous_element = None
    for element in number_list:
        if previous_element is None:
            previous_element = element
            continue
        if element > previous_element:
            previous_element = element
        else:
            return 'NO'
    return 'YES'


with open('input.txt') as file:
    number_list = map(int, file.read().split())

with open('output.txt', 'w') as file:
    file.write(is_list_ascending(number_list))
