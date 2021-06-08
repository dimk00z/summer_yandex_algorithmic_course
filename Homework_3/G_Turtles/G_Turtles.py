with open('input.txt') as file:
    lines = file.readlines()
    turtles_number = int(lines[0])
    number_of_true = 0
    said_true = set()
    for line in lines[1:]:
        if len(line) > 2:
            before, after = tuple(map(int, line.split()))
            positive = before >= 0 and after >= 0
            correct_input = before < turtles_number and after < turtles_number
            correct_number_of_turtles = (before+after) == turtles_number-1
            if positive and correct_input and correct_number_of_turtles \
                    and (before, after) not in said_true:
                said_true.add((before, after))
                number_of_true += 1


with open('output.txt', 'w') as file:
    file.write(str(number_of_true))
