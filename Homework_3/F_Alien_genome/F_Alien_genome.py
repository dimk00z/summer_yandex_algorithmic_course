with open('input.txt') as file:

    lines = file.readlines()
    DNA_1 = lines[0].strip()
    DNA_2 = lines[1].strip()
    count = 0
    for position in range(len(lines[0])-2):
        current_genome = lines[0][position:position+2]
        count += DNA_2.count(current_genome)
    # print(count)
with open('output.txt', 'w') as file:
    file.write(str(count))
