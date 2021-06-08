def get_points(t, d, n, coordinates) -> str:
    possible_points = set()
    for coordinate in coordinates[:n-1]:
        print(coordinate)
    return '  jklj  '


with open('input.txt') as file:
    lines = file.readlines()
    t, d, n = tuple(map(int, lines[0].split()))
    coordinates = []
    for line in lines[1:]:
        coordinates.append(list(map(int, line.split())))

with open('output.txt', 'w') as file:
    file.write(get_points(t, d, n, coordinates))
