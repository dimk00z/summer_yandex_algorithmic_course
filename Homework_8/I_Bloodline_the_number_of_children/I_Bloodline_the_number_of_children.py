import sys

sys.setrecursionlimit(100000)


class Person():
    def __init__(self, name):
        self.name = name
        self.parent = None
        self.kids = []
        self.kids_count = 0

    def __str__(self) -> str:
        kids = ' '.join([kid.name for kid in self.kids])
        return f'{self.name} : {kids}'


def get_bloodline(person):
    kids_count = person.kids_count

    def get_descendants_count(person):
        nonlocal kids_count

        for kid in person.kids:
            kids_count += kid.kids_count
            get_descendants_count(kid)

    get_descendants_count(person)

    return kids_count


persons = {}
with open('input.txt') as file:
    lines = file.readlines()
    for line in lines[1:]:
        child, parent = line.split()
        if parent not in persons:
            persons[parent] = Person(parent)
        if child not in persons:
            persons[child] = Person(child)
        persons[child].parent = persons[parent]
        persons[parent].kids.append(persons[child])
        persons[parent].kids_count += 1

del lines
result = []
for person in persons:
    children = get_bloodline(persons[person])
    result.append(f'{person} {children}')
result.sort()


with open('output.txt', 'w') as file:
    file.write('\n'.join(result))
