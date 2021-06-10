with open('input.txt') as file:
    lines = file.readlines()
keyboard_buttons = int(lines[0])
buttons = {str(button_position+1): int(presses)
           for button_position, presses in enumerate(lines[1].split())}
presses_number = int(lines[2])
for press in lines[3].split():
    buttons[press] -= 1
result = []
for button_position in range(keyboard_buttons):
    is_broken = 'NO' if buttons[str(button_position+1)] >= 0 else "YES"
    result.append(is_broken)

with open('output.txt', 'w') as file:
    file.write('\n'.join(result))
