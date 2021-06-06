

def create_mine_field(n, m, mines):
    mine_field = [
        [0 for _ in range(m)
         ] for _ in range(n)
    ]
    for mine in mines:
        x, y = mine
        mine_field[x-1][y-1] = '*'
    return mine_field


def neighbours(i, j, m):
    nearest = [m[x][y] for x in [i-1, i, i+1] for y in [j-1, j, j+1]
               if x in range(0, len(m)) and y in range(0, len(m[x]))
               and (x, y) != (i, j)]
    nearest_count = nearest.count('*')
    return nearest_count


def check_field(mine_field, n, m):
    for x in range(n):
        for y in range(m):
            if mine_field[x][y] == '*':
                continue
            else:
                mine_field[x][y] = neighbours(i=x, j=y, m=mine_field)


with open('input.txt') as file:
    lines = file.readlines()
    n, m, k = list(map(int, lines[0].split()))
    mines = []
    for line in lines[1::]:
        mines.append(list(map(int, line.split())))


mine_field = create_mine_field(n, m, mines)
check_field(mine_field, n, m)

with open('output.txt', 'w') as file:
    rows = []
    for row in mine_field:
        line = f"{' '.join([str(item) for item in row])}\n"
        rows.append(line)
    file.writelines(rows)
