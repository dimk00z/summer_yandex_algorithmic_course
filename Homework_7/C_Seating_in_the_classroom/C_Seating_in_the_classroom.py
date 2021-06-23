def calculate_variants(n, d, x):
    line_with_distance = []
    final_students = [0]*n
    for student_position, student in enumerate(x):
        line_with_distance.append(
            (student - d, -1))
        line_with_distance.append(
            (student, 0, str(student_position)))
        line_with_distance.append(
            (student + d, 1))
    line_with_distance.sort()
    count = 0
    last_count = 0
    current_variant = 0

    for point in line_with_distance:
        count += point[1]*-1
        if count == 0 or last_count > count:
            current_variant = 0
        if point[1] == 0:
            if current_variant == 0:
                current_variant = 1
            final_students[int(point[2])] = current_variant
            print(point[0], point[2], current_variant)
            current_variant += 1
        last_count = count

    result = []
    result.append(str(max(final_students)))
    result.append(' '.join(map(str, final_students)))
    return '\n'.join(result)


with open('input.txt') as file:
    lines = file.readlines()
    # n -students, d - distance between students
    n, d = map(int, lines[0].split())
    # x - students position
    x = list(map(int, lines[1].split()))


with open('output.txt', 'w') as file:
    file.write(calculate_variants(n, d, x))
