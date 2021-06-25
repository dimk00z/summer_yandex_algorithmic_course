# идея от jasfex

child_for_key = {}
parent_for_key = {}
with open('input.txt') as file:
    lines = file.readlines()
    n = int(lines[0])
for line in lines[1:]:
    child, parent = line.split()
    parent_for_key[child] = parent
    if parent not in child_for_key:
        child_for_key[parent] = []
    child_for_key[parent].append(child)

# поиск корня дерева
queue = list(set(child_for_key.keys())-set(parent_for_key.keys()))

ordered_siblings = []
while len(queue) > 0:
    name = queue.pop(0)
    ordered_siblings.append(name)
    if name in child_for_key:
        queue.extend(child_for_key[name])

bloodline_count = {name: 0 for name in ordered_siblings}
for name in ordered_siblings[-1::-1]:
    if name in child_for_key:
        chilrden = child_for_key[name]
        for child in chilrden:
            bloodline_count[name] += 1+bloodline_count[child]
result = []
for name in sorted(ordered_siblings):
    result.append(f'{name} {bloodline_count[name]}')

with open('output.txt', 'w') as file:
    file.write('\n'.join(result))
