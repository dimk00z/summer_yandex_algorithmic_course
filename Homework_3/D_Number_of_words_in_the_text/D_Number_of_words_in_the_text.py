with open('input.txt') as file:
    final_set = set()
    for line in file.readlines():
        final_set |= set(line.split())


with open('output.txt', 'w') as file:
    file.write(str(len(final_set)))
