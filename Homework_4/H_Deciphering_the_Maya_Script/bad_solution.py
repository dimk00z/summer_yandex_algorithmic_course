'''
It is bad for time solution
'''
with open('input.txt') as file:
    lines = file.readlines()

g, s = tuple(map(int, lines[0].split()))
letter_sequence = list(lines[1].strip())
word = list(lines[2].strip())

counter = 0
difference = s-g

buf_sequence = letter_sequence.copy()

for position, letter in enumerate(word):
    if position <= difference:
        if letter in buf_sequence:
            buf_sequence.pop(buf_sequence.index(letter))
            check = position+1
            while buf_sequence:
                if word[check] in buf_sequence:
                    buf_sequence.pop(
                        buf_sequence.index(word[check]))
                    check += 1
                else:
                    break
            if not buf_sequence:
                counter += 1
        buf_sequence = letter_sequence.copy()


with open('output.txt', 'w') as file:
    file.write(str(counter))
