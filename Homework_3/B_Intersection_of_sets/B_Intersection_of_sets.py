from functools import reduce

with open('input.txt') as file:
    intersection = reduce(set.intersection,  [
        set(map(int, line.split())) for line in file.readlines()])
    intersection = ' '.join(list(map(str, sorted(list(intersection)))))


with open('output.txt', 'w') as file:
    file.write(intersection)
