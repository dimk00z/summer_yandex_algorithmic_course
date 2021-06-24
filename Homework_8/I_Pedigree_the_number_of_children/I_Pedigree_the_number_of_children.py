import sys

sys.setrecursionlimit(100000)


class Person():
    def __init__(self, name):
        self.name = name
        self.parent = None
        self.kids = []

    def __str__(self) -> str:
        kids = ' '.join([kid.name for kid in self.kids])
        return f'{self.name} : {kids}'


def get_pedigree(person):

    def get_descendants(person, descendants=None):
        if descendants is None:
            descendants = set()
        for kid in person.kids:
            descendants.add(kid)
            get_descendants(kid, descendants)
        return descendants
    return len(get_descendants(person))


persons = {}
with open('input.txt') as file:
    lines = file.readlines()
    # n = int(lines[0])
    parents_for_check = set()
    for line in lines[1:]:
        child, parent = line.split()
        parents_for_check.add(child)
        parents_for_check.add(parent)
        if parent not in persons:
            persons[parent] = Person(parent)
        if child not in persons:
            persons[child] = Person(child)
        persons[child].parent = persons[parent]
        persons[parent].kids.append(persons[child])
del lines
result = []
for parent in parents_for_check:
    children = get_pedigree(persons[parent])
    result.append(f'{parent} {children}')
result.sort()

with open('output.txt', 'w') as file:
    file.write('\n'.join(result))
