from functools import reduce
from random import randint

with open('input.txt') as file:
    lines = [line.strip() for line in file.readlines()]
    students_number = int(lines[0])
    last_student = 0
    studens = {}
    for line in lines[1:]:
        if line.isdigit():
            last_student = str(int(last_student)+1)
            studens[last_student] = set()
            continue
        else:
            studens[last_student].add(line)
    all_known = reduce(set.intersection, [
                       language for student, language in studens.items()])
    somebody_known = reduce(set.union, [
        language for _, language in studens.items()])

with open('output.txt', 'w') as file:
    file.write(f'{str(len(all_known))}\n')
    for language in all_known:
        file.write(f'{language}\n')

    file.write(f'{str(len(somebody_known))}\n')
    for language in somebody_known:
        file.write(f'{language}\n')
