def count(a, b, c):
    if not a and not b and not c:
        return '1'
    sum = 2 * a + 3 * b + 4 * c
    cnt = a + b + c
    l = 0
    r = cnt + 1
    while l < r:
        m = (l + r) // 2
        if (sum + 5 * m) / (cnt + m) < 3.5:
            l = m + 1
        else:
            r = m
    return str(l)


with open('input.txt') as file:
    lines = file.readlines()
    a = int(lines[0])
    b = int(lines[1])
    c = int(lines[2])


with open('output.txt', 'w') as file:
    file.write(count(a, b, c))
