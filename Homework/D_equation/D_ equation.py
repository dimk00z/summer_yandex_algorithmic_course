def solve_the_equation(a, b, c) -> str:
    if (c < 0) or (a == 0 and b != c**2):
        return 'NO SOLUTION'
    if (a == b == c == 0) or (a == 0 and b == c**2):
        return 'MANY SOLUTIONS'
    if (c**2 - b) % a == 0:
        return str(int((c**2 - b)/a))
    else:
        return 'NO SOLUTION'


with open('input.txt') as file:
    a, b, c = [int(line.strip()) for line in file.readlines()]

with open('output.txt', 'w') as file:
    file.write(solve_the_equation(a, b, c))

# a, b, c = int(input()), int(input()), int(input())
# print(solve_the_equation(a, b, c))
