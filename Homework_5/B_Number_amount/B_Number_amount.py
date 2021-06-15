def count_numbers(cars_number, lucky_number, cars_numbers):
    result = 0
    for current_position, number in enumerate(cars_numbers):
        if number == lucky_number:
            result += 1


with open('input.txt') as file:
    lines = file.readlines()
    cars_number, lucky_number = map(int, lines[0].split())
    cars_numbers = [int(color) for color in lines[1].split()]


with open('output.txt', 'w') as file:
    file.write(count_numbers(cars_number, lucky_number, cars_numbers))
