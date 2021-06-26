def calculate_variants(k, commands):
    ans = 0
    prevlen = 0
    for i in range(k, len(commands)):
        if commands[i] == commands[i-k]:
            prevlen += 1
            ans += prevlen
        else:
            prevlen = 0
    return ans


with open('input.txt') as file:
    lines = file.readlines()
    k = int(lines[0])
    commands = lines[1].strip()


with open('output.txt', 'w') as file:
    file.write(str(calculate_variants(k, commands)))
