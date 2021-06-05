def calculate_the_nearest(number_list, current_number) -> int:
    nearest = number_list[0]
    for element in number_list:
        if abs(current_number-element) < abs(current_number-nearest):
            nearest = element
    return nearest


with open('input.txt') as file:
    lines = file.readlines()
    number_list = list(map(int, lines[1].split()))
    current_number = int(lines[2])

with open('output.txt', 'w') as file:
    file.write(str(calculate_the_nearest(number_list, current_number)))
