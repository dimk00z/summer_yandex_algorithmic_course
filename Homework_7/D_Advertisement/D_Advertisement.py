def calculate_ads(n, events):
    events.sort()
    # print(n, events)
    if len(events) == 0:
        return '0 10 20'
    elif len(events) == 2:
        return f'1 {events[0][0]} {events[0][0]+10}'
    bestans = 0
    firstbest, secondbest = 0, 0
    firstad = set()
    for i in range(len(events)):
        event1 = events[i]
        if event1[1] == -1:
            firstad.add(event1[2])
            if len(firstad) > bestans:
                bestans = len(firstad)
                firstbest = event1[0]
                secondbest = event1[0]+5
        secondadcnt = 0
        for j in range(i+1, len(events)):
            event2 = events[j]
            if event2[1] == -1 and event2[2] not in firstad:
                secondadcnt += 1
            if event2[0]-5 >= event1[0] and len(firstad)+secondadcnt > bestans:
                bestans = len(firstad)+secondadcnt
                firstbest = event1[0]
                secondbest = event2[0]
            if event2[1] == 1 and event2[2] not in firstad:
                secondadcnt -= 1
        if event1[1] == 1:
            firstad.remove(event1[2])
    return f'{bestans} {firstbest} {secondbest}'


with open('input.txt') as file:
    lines = file.readlines()
    n = int(lines[0])
    events = []
    for event_number, time in enumerate(lines[1:]):
        start, end = map(int, time.split())
        if end-start >= 5:
            events.append((start, -1, event_number))
            events.append((end-5, 1, event_number))


with open('output.txt', 'w') as file:
    file.write(calculate_ads(n, events))
