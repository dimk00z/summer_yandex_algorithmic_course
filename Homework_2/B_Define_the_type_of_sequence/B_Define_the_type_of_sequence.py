def define_sequence_type(sequence) -> str:

    asc = True
    cnst = True
    desc = True
    weak = False

    previous_element = sequence[0]
    if previous_element == -2000000000:
        return 'CONSTANT'
    for element in sequence[1:]:
        if element == -2000000000:
            break
        cnst &= element == previous_element
        weak |= element == previous_element
        asc &= element >= previous_element
        desc &= element <= previous_element
        previous_element = element

    if cnst:
        return 'CONSTANT'
    elif asc:
        return 'WEAKLY ASCENDING' if weak else 'ASCENDING'
    elif desc:
        return 'WEAKLY DESCENDING' if weak else 'DESCENDING'
    else:
        return 'RANDOM'


with open('input.txt') as file:
    sequence = list(map(int, file.readlines()))

with open('output.txt', 'w') as file:
    file.write(define_sequence_type(sequence))
