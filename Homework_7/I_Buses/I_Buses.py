def makeminutes(time):
    h, m = time.split(':')
    return int(h)*60+int(m)


def check_buses(n, m, lines):
    cntbuses = [0]*(n+1)
    busbalance = [0]*(n+1)
    events = []
    overnight = 0
    for line in lines:
        cdep, deptime, carr, arrtime = line.split()
        cdep = int(cdep)
        carr = int(carr)
        deptime = makeminutes(deptime)
        arrtime = makeminutes(arrtime)
        if arrtime < deptime:
            overnight += 1
        busbalance[cdep] -= 1
        busbalance[carr] += 1
        events.append((deptime, 1, cdep))
        events.append((arrtime, -1, carr))
    disbalance = False
    for i in range(n+1):
        if busbalance[i] != 0:
            disbalance = True
    if disbalance:
        return '-1'
    events.sort()
    for event in events:
        if event[1] == -1:
            cntbuses[event[2]] += 1
        else:
            if cntbuses[event[2]] > 0:
                cntbuses[event[2]] -= 1
    ans = 0
    for i in range(n+1):
        ans += cntbuses[i]
    return str(ans+overnight)


with open('input.txt') as file:
    lines = file.readlines()
    n, m = map(int, lines[0].split())


with open('output.txt', 'w') as file:
    file.write(check_buses(n, m, lines[1:]))
