

def get_table_size(
        a1, b1,
        a2, b2):
    tables = [
        [a1+a2, max(b1, b2)],
        [a1+b2, max(b1, a2)],

        [b1+b2, max(a1, a2)],
        [b1+a2, max(a1, b2)],
    ]
    min_table = tables[0]
    min_square = min_table[0]*min_table[1]
    for table in tables:
        if min_table is table:
            continue
        current_square = table[0]*table[1]
        if current_square < min_square:
            min_table = table
            min_square = current_square
    return min_table


with open('input.txt') as file:
    a1, b1, a2, b2 = map(
        int, file.read().split())

with open('output.txt', 'w') as file:
    file.write(' '.join(map(str, get_table_size(a1, b1, a2, b2))))
