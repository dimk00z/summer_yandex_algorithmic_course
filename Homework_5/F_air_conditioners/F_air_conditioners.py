def calculate_powers(n, powers, m, air_cons):
    cost = 0
    current_con = 0

    for power in powers:
        while current_con < len(air_cons):
            conditioner_price, conditioner_power = air_cons[current_con]
            if conditioner_power >= power:
                cost += conditioner_price
                break
            else:
                current_con += 1

    return cost


with open('input.txt') as file:
    lines = file.readlines()
    n = int(lines[0])
    powers = list(map(int, lines[1].split()))
    powers.sort()
    m = int(lines[2])
    air_cons = []
    for line in lines[3:]:
        conditioner_power, conditioner_price = tuple(map(int, line.split()))
        air_cons.append([conditioner_price, conditioner_power])
    air_cons.sort()


with open('output.txt', 'w') as file:
    file.write(str(calculate_powers(n, powers, m, air_cons)))
