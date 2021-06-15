def choose_clothes(t_shirt_number,
                   t_shirt_colors, pants_number, pants_colors):
    t_shirt_min_position = pants_min_position = 0
    t_shirt_current_position = pants_current_position = 0
    difference = abs(t_shirt_colors[0]-pants_colors[0])
    while True:
        if (t_shirt_current_position >= t_shirt_number) | (pants_current_position >= pants_number):
            break
        if t_shirt_colors[t_shirt_current_position] == pants_colors[pants_current_position]:
            t_shirt_min_position = t_shirt_current_position
            pants_min_position = pants_current_position
            break
        if abs(t_shirt_colors[t_shirt_current_position]-pants_colors[pants_current_position]) < difference:
            difference = abs(
                t_shirt_colors[t_shirt_current_position]-pants_colors[pants_current_position])
            t_shirt_min_position = t_shirt_current_position
            pants_min_position = pants_current_position
        if t_shirt_colors[t_shirt_current_position] < pants_colors[pants_current_position]:
            t_shirt_current_position += 1
        else:
            pants_current_position += 1
    return f'{t_shirt_colors[t_shirt_min_position]} {pants_colors[pants_min_position]}'


with open('input.txt') as file:
    lines = file.readlines()
    t_shirt_number = int(lines[0])
    t_shirt_colors = [int(color) for color in lines[1].split()]
    pants_number = int(lines[2])
    pants_colors = [int(color) for color in lines[3].split()]

with open('output.txt', 'w') as file:
    file.write(choose_clothes(t_shirt_number,
               t_shirt_colors, pants_number, pants_colors))
