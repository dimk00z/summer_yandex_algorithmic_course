def choose_monument(n, r, d_list):
    i, j, count = 0, 1, 0

    while j < len(d_list) and i < len(d_list) - 1:
        if d_list[j] - d_list[i] <= r:
            j += 1
        else:
            count += n - j
            i += 1
    return count


with open('input.txt') as file:
    lines = file.readlines()
    n, r = map(int, lines[0].split())
    d_list = [int(distance) for distance in lines[1].split()]


with open('output.txt', 'w') as file:
    file.write(str(choose_monument(n, r, d_list)))
