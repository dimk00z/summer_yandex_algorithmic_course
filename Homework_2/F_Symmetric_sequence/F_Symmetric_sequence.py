def calculate_simmetric_sequence(sequence, length):
    position = length
    step = 0
    required_sequence = []
    while sequence != sequence[::-1]:
        sequence.insert(position, sequence[step])
        required_sequence.append(sequence[step])
        step += 1
    return f'{step}\n{" ".join(map(str,required_sequence[::-1]))}'


with open('input.txt') as file:
    lines = file.readlines()
    length = int(lines[0])
    sequence = list(map(int, lines[1].split()))

with open('output.txt', 'w') as file:
    file.write(calculate_simmetric_sequence(sequence, length))
