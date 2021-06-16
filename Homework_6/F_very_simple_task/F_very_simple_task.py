def calculate_time(n, x, y):
    left, right = 0, (n - 1) * max(x, y)
    while right > left + 1:
        middle = (right + left) // 2
        if (middle // x + middle // y) < n - 1:
            left = middle
        else:
            right = middle
    return right + min(x, y)


with open('input.txt') as file:
    n, x, y = map(int, file.readlines()[0].split())


with open('output.txt', 'w') as file:
    file.write(str(calculate_time(n, x, y)))
