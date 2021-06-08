from functools import reduce


def set_colors_to_str(current_set, result):
    result.append(str(len(current_set)))
    result.append(' '.join(map(str, sorted(list(current_set)))))


def get_colors_results(Anya_colors, Borya_colors) -> str:
    result = []
    colors_intersection = reduce(set.intersection, [Anya_colors, Borya_colors])
    set_colors_to_str(colors_intersection, result)

    Anya_unique_colors = Anya_colors - Borya_colors
    set_colors_to_str(Anya_unique_colors, result)

    Borya_unique_colors = Borya_colors - Anya_colors
    set_colors_to_str(Borya_unique_colors, result)

    return '\n'.join(result)


with open('input.txt') as file:
    lines = file.readlines()
    n, m = tuple(map(int, lines[0].split()))
    Anya_colors = set([int(color) for color in lines[1:n+1]])
    Borya_colors = set([int(color) for color in lines[n+1:]])


with open('output.txt', 'w') as file:
    file.write(get_colors_results(Anya_colors, Borya_colors))
