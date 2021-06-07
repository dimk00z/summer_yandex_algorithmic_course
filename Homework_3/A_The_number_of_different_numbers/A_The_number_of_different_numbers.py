with open('input.txt') as file:
    number_list = set(map(int, file.read().split()))

with open('output.txt', 'w') as file:
    file.write(str(len(number_list)))
