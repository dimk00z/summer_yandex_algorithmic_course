with open('input.txt') as file:

    x_positions = set()
    for line in file.readlines()[1:]:
        x_positions.add(int(line.split()[0]))
    shoots = len(x_positions)


with open('output.txt', 'w') as file:
    file.write(str(shoots))
