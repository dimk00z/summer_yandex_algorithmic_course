def get_music_interval(sheet_music_number, first_note, notes):
    previous_hz = first_note
    left_border_hz, right_border_hz = 30, 4000
    for note_line in notes:
        current_hz, option = note_line.split()
        current_hz = float(current_hz)
        if previous_hz == current_hz:
            continue
        mid = (previous_hz+current_hz)/2
        if current_hz > previous_hz and option == 'closer' or \
                current_hz < previous_hz and option != 'closer':
            left_border_hz = max(left_border_hz, mid)
        else:
            right_border_hz = min(right_border_hz, mid)
        previous_hz = current_hz
    return f'{float(left_border_hz)} {float(right_border_hz)}'


with open('input.txt') as file:
    lines = file.readlines()
    sheet_music_number = int(lines[0])
    first_note = float(lines[1])
    notes = list(lines[2:])

with open('output.txt', 'w') as file:
    file.write(get_music_interval(sheet_music_number, first_note, notes))
