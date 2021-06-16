

def count_numbers(cars_number, lucky_number, cars_numbers):
    cnt = 0
    prev_sum = None
    prev_j = None
    sm = 0
    for i in range(cars_number):
        if prev_j:
            j = prev_j
            sm = prev_sum - cars_numbers[i-1] - cars_numbers[j]
        else:
            j = i
            sm = 0
        while True:
            sm += cars_numbers[j]
            if sm == lucky_number:
                cnt += 1
                prev_sum = sm
                prev_j = j
                break
            elif sm > lucky_number:
                prev_sum = sm
                prev_j = j
                break
            j += 1
            if j == cars_number:
                return cnt
    return cnt


with open('input.txt') as file:
    lines = file.readlines()
    cars_number, lucky_number = map(int, lines[0].split())
    cars_numbers = [int(color) for color in lines[1].split()]


with open('output.txt', 'w') as file:
    file.write(str(count_numbers(cars_number, lucky_number, cars_numbers)))
