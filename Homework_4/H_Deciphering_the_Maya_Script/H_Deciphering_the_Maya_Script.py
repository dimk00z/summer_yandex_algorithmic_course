with open('input.txt') as file:
    lines = file.readlines()

g, s = tuple(map(int, lines[0].split()))
letter_sequence = set(lines[1].strip())
word = lines[2].strip()
counter = 0
check_letter = 0
previous_in = False
difference = s-g

for position, letter in enumerate(word):
    if letter in letter_sequence:

        if position < difference:
            check = 1
            for i in range(1, g+1):
                next_letter = word[position+i]
                if next_letter not in letter_sequence:
                    break
                check += 1
                print(check)
            if check == g:
                counter += 1


print(counter)
