def get_tools(N, K, M):
    tools_count = 0

    def melt(K, M):
        nonlocal N, tools_count
        tools_per_blank = K//M
        tools_remainder = K % M
        while (N >= K):

            blank_count = N//K
            N = N % K + blank_count*tools_remainder
            tools_count += blank_count * tools_per_blank
    if M <= K:
        melt(K, M)
    return str(tools_count)


with open('input.txt') as file:
    N, K, M = map(int, file.read().split())

with open('output.txt', 'w') as file:
    file.write(get_tools(N, K, M))

print(get_tools(10, 5, 2))
print(get_tools(13, 5, 3))
print(get_tools(14, 5, 3))
print(get_tools(200, 10, 3))
