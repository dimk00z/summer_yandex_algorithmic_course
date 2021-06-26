def calculate_triangles(n, points):
    ans = 0
    # print(n, points)
    for i in range(n):
        usedvectors = set()
        neig = []
        for j in range(n):
            vecx = points[i][0] - points[j][0]
            vecy = points[i][1] - points[j][1]
            veclen = vecx**2+vecy**2
            neig.append(veclen)
            if (vecx, vecy) in usedvectors:
                ans -= 1
            usedvectors.add((-vecx, -vecy))
        neig.sort()
        r = 0
        for l in range(len(neig)):
            while r < len(neig) and neig[l] == neig[r]:
                r += 1
            ans += r-l-1
    return ans


with open('input.txt') as file:
    lines = file.readlines()
    n = int(lines[0])
    points = [tuple(map(int, line.split())) for line in lines[1:]]

with open('output.txt', 'w') as file:
    file.write(str(calculate_triangles(n, points)))
