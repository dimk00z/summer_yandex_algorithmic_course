with open('input.txt') as file:
    lines = file.readlines()
blocks_number = int(lines[0])
pyramid = {}
for line in lines[1:]:
    heigth, weight = map(int, line.split())
    pyramid[heigth] = max(pyramid.get(heigth, weight), weight)


with open('output.txt', 'w') as file:
    file.write(str(sum(pyramid.values())))
