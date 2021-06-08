'''
Решение не мое, взял тут
https://github.com/EvgenyEmets/Yandex-algorithm-training/blob/7e865f0e11baa5d47ec82815f7ba67dfda0f5843/Contest_1/E.py
'''


def comp(k1, m, k2, p2, n2):
    posibleN = list()
    for i in range(k2):
        mint = (p2 - 1) * i * m + i * (n2 - 1)
        maxt = mint + i
        if k2 > mint and k2 <= maxt:
            posibleN.append(i)
        if k2 < mint:
            break
    P = list()
    N = list()
    for i in posibleN:
        p = k1 // (m * i) + 1
        if k1 % (m*i) == 0:
            p -= 1
        n = (k1 - (p - 1) * m * i) // i + 1
        if(k1 - (p - 1) * m * i) % i == 0:
            n -= 1
        if p not in P:
            P.append(p)
        if n not in N:
            N.append(n)
    if len(P) != 1:
        p1 = 0
    else:
        p1 = P[0]
    if len(N) != 1:
        n1 = 0
    else:
        n1 = N[0]
    return p1, n1


k1, m, k2, p2, n2 = map(int, input().split())
posibleN = list()
for i in range(k2):
    mint = (p2 - 1) * i * m + i * (n2 - 1)
    maxt = mint + i
    if k2 > mint and k2 <= maxt:
        posibleN.append(i)
    if k2 < mint:
        break
if k2 <= (p2 - 1) * m + n2 - 1 or (n2 != 1 and len(posibleN) == 0) or n2 > m:
    p1 = -1
    n1 = -1
elif k1 == k2:
    p1, n1 = p2, n2
elif p2 == 1:
    if n2 == 1:
        if k1 > k2 * m:
            p1 = 0
            if m == 1:
                n1 = 1
            else:
                n1 = 0
        else:
            p1 = 1
            if m == 1 or k1 < k2:
                n1 = 1
            else:
                n1 = 0
    else:
        if k1 < k2:
            p1 = 1
            if k2 == n2:
                n1 = k1
            else:
                posibleN = list()
                for i in range(k2):
                    if i*(n2-1) < k2 and i*n2 >= k2:
                        posibleN.append(i)
                    if i*(n2-1) > k2:
                        break
                N = list()
                for i in posibleN:
                    n = k1 // i
                    if k1 % i != 0:
                        n += 1
                    if n not in N:
                        N.append(n)
                if len(N) != 1:
                    n1 = 0
                else:
                    n1 = N[0]
        elif k1 <= (k2 // n2 + 1) * m:
            p1 = 1
            N = list()
            for i in posibleN:
                n = k1 // i
                if k1 % i != 0:
                    n += 1
                if n not in N:
                    N.append(n)
            if len(N) == 1:
                n1 = N[0]
            else:
                n1 = 0
        else:
            p1, n1 = comp(k1, m, k2, p2, n2)
else:
    p1, n1 = comp(k1, m, k2, p2, n2)

print(p1, n1)
