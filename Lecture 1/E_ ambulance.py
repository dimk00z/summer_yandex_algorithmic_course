def get_P1_and_N1(K1, M, K2, P2, N2):
    P1 = 0
    N1 = 0
    return (P1, N1)


with open('input.txt') as file:
    K1, M, K2, P2, N2 = map(int, file.read().split())


print(K1, M, K2, P2, N2)
P1, N1 = get_P1_and_N1(K1, M, K2, P2, N2)
print(P1, N1)
