def count_neighbors(number_list):
    neighbors_count = 0
    for element_position, element in enumerate(number_list[1:-1:]):
        if (element > number_list[element_position]) \
                and (element > number_list[element_position+2]):

            neighbors_count += 1
    return str(neighbors_count)


with open('input.txt') as file:
    number_list = list(map(int, file.read().split()))


with open('output.txt', 'w') as file:
    file.write(count_neighbors(number_list))
