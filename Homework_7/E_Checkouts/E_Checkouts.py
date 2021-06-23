def calculate_time(n, times):
    events = []
    count = 0
    for time in times:
        t1 = time[0]*60+time[1]
        t2 = time[2]*60+time[3]
        events.append((t1, 1))
        events.append((t2, -1))
        if t1 >= t2:
            count += 1
    ans = 0
    start = 0
    for x, type in sorted(events):
        count += type
        if count == n:
            start = x
        if count == n-1 and type == -1:
            ans += x-start
    if count == n:
        ans += 24*60-start
    return str(ans)


with open('input.txt') as file:
    lines = file.readlines()
    # n -checkouts, d - distance between students
    n = int(lines[0])
    times = [tuple(map(int, line.split())) for line in lines[1:]]
del lines

with open('output.txt', 'w') as file:
    file.write(calculate_time(n, times))
