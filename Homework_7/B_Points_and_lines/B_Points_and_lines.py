

with open('input.txt') as file:
    lines = file.readlines()
    # n -lines, m - points
    n, m = map(int, lines[0].split())
    points = list(map(int, lines[-1].split()))
    lines = [tuple(map(int, line.split())) for line in lines[1:n+1]]
result = ['']*m
hole_line = []
for line in lines:
    hole_line.append((line[0], -1))
    hole_line.append((line[1], 1))
for point_position in range(m):
    hole_line.append((points[point_position], 0, str(point_position)))
hole_line.sort()
count = 0
for point in hole_line:
    count += point[1]*-1
    if point[1] == 0:
        result[int(point[2])] = str(count)


with open('output.txt', 'w') as file:
    file.write(' '.join(result))
