def calculate(n, m, lines, points):
    # print(n, m, lines, points)
    result = []
    for point in points:
        point_count = 0
        for line in lines:
            if min(line[0], line[1]) <= point and point <= max(line[0], line[1]):
                point_count += 1
        result.append(str(point_count))

    return ' '.join(result)


with open('input.txt') as file:
    lines = file.readlines()
    # n -lines, m - points
    n, m = map(int, lines[0].split())
    points = list(map(int, lines[-1].split()))
    lines = [tuple(map(int, line.split())) for line in lines[1:n+1]]


with open('output.txt', 'w') as file:
    file.write(calculate(n, m, lines, points))
