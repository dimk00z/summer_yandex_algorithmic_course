

def count_desk(w, h, n):
    left = max(w, h)
    right = left * n
    while right - left > 1:
        middle = (right + left) // 2
        res = (middle // w) * (middle // h)
        if res < n:
            left = middle
        else:
            right = middle
    return str(right)


with open('input.txt') as file:
    lines = file.readlines()
    w, h, n = map(int, lines[0].split())

with open('output.txt', 'w') as file:
    file.write(count_desk(w, h, n))
