'''
Решение не мое, взял тут
https://github.com/EvgenyEmets/Yandex-algorithm-training/blob/7e865f0e11baa5d47ec82815f7ba67dfda0f5843/Contest_3/J.py
'''


def newcorner(c, t):
    c[0][1] += t
    c[1][0] += t
    c[2][1] -= t
    c[3][0] -= t
    return c


def intersection_point(p1, p2, p3, p4):
    s1 = 0
    if (p1[0] - p2[0]) * (p1[1] - p2[1]) > 0:
        s1 = -1
    else:
        s1 = 1
    b1 = p1[1] + s1 * p1[0]
    s2 = 0
    if (p3[0] - p4[0]) * (p3[1] - p4[1]) > 0:
        s2 = -1
    else:
        s2 = 1
    b2 = p3[1] + s2 * p3[0]
    if s1 == s2:
        return None
    else:
        x = (s1*b1 + s2*b2)/2
        y = (-1)*s1*x+b1
        if x <= max(p1[0], p2[0]) and x <= max(p3[0], p4[0])\
                and x >= min(p1[0], p2[0]) and x >= min(p3[0], p4[0])\
        and y <= max(p1[1], p2[1]) and y <= max(p3[1], p4[1])\
            and y >= min(p1[1], p2[1]) and y >= min(p3[1], p4[1]):
            return [x, y]
        else:
            return None


def between(p, r):
    return p[1] - p[0] >= r[2][1] - r[2][0] and \
        p[1] - p[0] <= r[0][1] - r[0][0] and \
        p[0]+p[1] >= r[3][0]+r[3][1] and \
        p[0]+p[1] <= r[1][0]+r[1][1]


def up(a, b, c, d):
    if a[1] > b[1] and a[1] > c[1] and a[1] > d[1]:
        return a
    elif b[1] > c[1] and b[1] > d[1]:
        return b
    elif c[1] > d[1]:
        return c
    else:
        return d


def right(a, b, c, d):
    if a[0] > b[0] and a[0] > c[0] and a[0] > d[0]:
        return a
    elif b[0] > c[0] and b[0] > d[0]:
        return b
    elif c[0] > d[0]:
        return c
    else:
        return d


def down(a, b, c, d):
    if a[1] < b[1] and a[1] < c[1] and a[1] < d[1]:
        return a
    elif b[1] < c[1] and b[1] < d[1]:
        return b
    elif c[1] < d[1]:
        return c
    else:
        return d


def left(a, b, c, d):
    if a[0] < b[0] and a[0] < c[0] and a[0] < d[0]:
        return a
    elif b[0] < c[0] and b[0] < d[0]:
        return b
    elif c[0] < d[0]:
        return c
    else:
        return d


def intersection(c1, c2):
    in_point = set()
    for i in range(4):
        for j in range(4):
            tmp = intersection_point(
                c1[i], c1[(i+1) % 4], c2[j], c2[(j+1) % 4])
            if tmp != None:
                in_point.add(tuple(tmp))
        if between(c1[i], c2):
            in_point.add(tuple(c1[i]))
        if between(c2[i], c1):
            in_point.add(tuple(c2[i]))
    corners = list(in_point)
    if len(corners) == 1:
        c = [[corners[0][0], corners[0][1]], [corners[0][0], corners[0][1]], [
            corners[0][0], corners[0][1]], [corners[0][0], corners[0][1]]]

    elif len(corners) == 2:
        c = [[0, 0], [0, 0], [0, 0], [0, 0]]
        if corners[0][1] < corners[1][1]:
            c[0] = [corners[1][0], corners[1][1]]
            c[2] = [corners[0][0], corners[0][1]]
        else:
            c[2] = [corners[1][0], corners[1][1]]
            c[0] = [corners[0][0], corners[0][1]]
        if corners[0][0] < corners[1][0]:
            c[1] = [corners[1][0], corners[1][1]]
            c[3] = [corners[0][0], corners[0][1]]
        else:
            c[3] = [corners[1][0], corners[1][1]]
            c[1] = [corners[0][0], corners[0][1]]
    elif len(corners) == 4:
        c = [[0, 0], [0, 0], [0, 0], [0, 0]]
        c[0] = list(up(*corners))
        c[1] = list(right(*corners))
        c[2] = list(down(*corners))
        c[3] = list(left(*corners))
    return c


def ans(c):
    result = []
    s = []
    for i in range(int(c[3][0]-1), int(c[1][0]+1)):
        for j in range(int(c[2][1]-1), int(c[0][1]+1)):
            p = [i, j]
            if between(p, c):
                s.append(p)
    result.append(str(len(s)))
    for i in s:
        result.append(' '.join(map(str, i)))
    return '\n'.join(result)


with open('input.txt') as file:
    lines = file.readlines()
    t, d, n = tuple(map(int, lines[0].split()))
    corner = [[0, 0], [0, 0], [0, 0], [0, 0]]  # up, right, down, left
    for iter in range(n):
        corner = newcorner(corner, t)
        p = list(map(int, lines[iter+1].split()))
        gps = [[p[0], p[1]], [p[0], p[1]], [p[0], p[1]], [p[0], p[1]]]
        gps = newcorner(gps, d)
        corner = intersection(corner, gps)

with open('output.txt', 'w') as file:
    file.write(ans(corner))
