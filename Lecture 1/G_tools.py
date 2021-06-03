def get_tools(N, K, M):
    tools_count = 0

    def melt(K, M):
        nonlocal N, tools_count
        while (N >= K):
            N -= K
            tools_count += K//M
            N += K % M
    melt(K, M)
    return str(tools_count)


with open('input.txt') as file:
    N, K, M = map(int, file.read().split())

with open('output.txt', 'w') as file:
    file.write(get_tools(N, K, M))

print(get_tools(10, 5, 2))
print(get_tools(13, 5, 3))
print(get_tools(14, 5, 3))
print(get_tools(200, 30, 3))
