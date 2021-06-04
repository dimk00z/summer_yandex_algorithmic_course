def check_brick(a, b, c, d, e) -> str:
    hole = [d, e]
    brick = [a, b, c]
    matrix = []
    result = 'NO'
    for value in hole:
        matrix.append([
            value >= brick_side_value for brick_side_value in brick
        ])

    for position_first_line, first_line_value in enumerate(matrix[0]):
        if not first_line_value:
            continue
        current_check = [
            second_line_value for position_second_line,
            second_line_value in enumerate(matrix[1])
            if position_first_line != position_second_line
        ]
        if any(current_check):
            result = 'YES'
    return result


with open('input.txt') as file:
    a, b, c, d, e = [int(line.strip()) for line in file.readlines()]

with open('output.txt', 'w') as file:
    file.write(check_brick(a, b, c, d, e))

print(
    check_brick(1, 1, 1, 1, 1)
)

print(
    check_brick(2, 2, 1, 1, 1)
)
