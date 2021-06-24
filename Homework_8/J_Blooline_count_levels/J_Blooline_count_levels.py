with open('input.txt') as file:
    lines = file.readlines()
    n = int(lines[0])
relationship = {}
levels = {}

for line in lines[1:]:
    child, parent = line.split()
    relationship[child] = parent
    levels[child] = 0
    levels[parent] = 0

for i in relationship:
    s = i
    while s in relationship:
        s = relationship[s]
        levels[i] += 1
result = []
for i in sorted(levels):
    result.append(f'{i} {levels[i]}')


with open('output.txt', 'w') as file:
    file.write('\n'.join(result))
