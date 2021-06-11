with open('input.txt') as file:
    lines = file.readlines()
    n, c, d = lines[0].split()
    text = [line.strip() for line in lines[1:]]

with open('output.txt', 'w') as file:
    file.write('answer')
