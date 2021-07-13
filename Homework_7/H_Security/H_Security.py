def check_security(k, lines):
    result = ['']*k
    for test_number, line in enumerate(lines):
        nums = list(map(int, line.split()))
        n = nums[0]
        events = [0]*(2*n)
        for i in range(1, len(nums), 2):
            events[i-1] = (nums[i], -1, i)
            events[i] = (nums[i+1], 1, i)
        events.sort()
        goodseq = set()
        nowseq = set()
        goodflag = True
        prevtime = -1
        for event in events:
            if event[0] != 0 and len(nowseq) == 0:
                goodflag = False
                break
            if len(nowseq) == 1 and event[0] != prevtime:
                goodseq.update(nowseq)
            if event[1] == -1:
                nowseq.add(event[2])
            else:
                nowseq.remove(event[2])
            prevtime = event[0]
        if events[-1][0] != 10000:
            goodflag = False
        if goodflag and len(goodseq) == n:
            result[test_number] = 'Accepted'
        else:
            result[test_number] = 'Wrong Answer'
    return '\n'.join(result)


with open('input.txt') as file:
    lines = file.readlines()
    k = int(lines[0])


with open('output.txt', 'w') as file:
    file.write(check_security(k, lines[1:]))
