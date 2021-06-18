def calculate_total_lifting_height(
        n, points, m, tracks):
    result = []
    left_prefixes = [0] + [None] * (n - 1)
    right_prefixes = [None] * (n - 1) + [0]
    for point_number in range(1, n):

        left_lifting = max(points[point_number][1] -
                           points[point_number-1][1], 0)

        left_prefixes[point_number] = \
            left_prefixes[point_number-1]+left_lifting

        right_lifting = max(points[n - point_number - 1]
                            [1] - points[n - point_number][1], 0)

        right_prefixes[n - point_number-1] = \
            right_prefixes[n - point_number] + right_lifting

    for track in tracks:
        if track[0] < track[1]:
            result.append(str(
                left_prefixes[track[1]-1]-left_prefixes[track[0]-1]
            ))
        else:
            result.append(str(
                right_prefixes[track[1]-1]-right_prefixes[track[0]-1]
            ))
    return '\n'.join(result)


with open('input.txt') as file:
    lines = file.readlines()
    n = int(lines[0])
    points = [tuple(map(int, line.split())) for line in lines[1:n+1]]
    m = int(lines[n+1])
    tracks = [tuple(map(int, line.split())) for line in lines[n+2:]]


with open('output.txt', 'w') as file:
    file.write(calculate_total_lifting_height(
        n, points, m, tracks))
