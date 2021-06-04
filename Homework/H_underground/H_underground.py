def calculate_times(a, b, n, m) -> str:
    min_time_for_first_line = (a+1)*n-a
    max_time_for_first_line = (a+1)*n+a
    min_time_for_sexond_line = (b+1)*m-b
    max_time_for_sexond_line = (b+1)*m+b
    if min_time_for_first_line > max_time_for_sexond_line \
            or min_time_for_sexond_line > max_time_for_first_line:
        return '-1'
    return ' '.join(
        map(str,
            (max(min_time_for_first_line, min_time_for_sexond_line),
             min(max_time_for_first_line, max_time_for_sexond_line))))


with open('input.txt') as file:
    a, b, n, m = [int(line.strip()) for line in file.readlines()]

with open('output.txt', 'w') as file:
    file.write(calculate_times(a, b, n, m))


# print(calculate_times(1, 3, 3, 2))
# print(calculate_times(1, 5, 1, 2))
