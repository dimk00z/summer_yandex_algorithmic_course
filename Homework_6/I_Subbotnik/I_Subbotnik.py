def check(m, check_params):
    min_brigades, c, heights = check_params
    i = 0
    brigates = 0
    while i < len(heights)-c+1:
        if heights[i+c-1]-heights[i] <= m:
            brigates += 1
            i += c
        else:
            i += 1
    return brigates >= min_brigades


def left_bin_search(l, r, check, check_params):
    while l < r:
        m = (l+r)//2
        if check(m, check_params):
            r = m
        else:
            l = m+1
    return l


with open('input.txt') as file:
    lines = file.readlines()
    _, r, c = tuple(map(int, lines[0].split()))
    heights = sorted([int(line) for line in lines[1:]])


with open('output.txt', 'w') as file:
    file.write(
        str(left_bin_search(0, heights[-1]-heights[0], check, (r, c, heights))))
