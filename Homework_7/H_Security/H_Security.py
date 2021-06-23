def check_security(full_security):
    result = []
    for security in full_security:
        count = 0
        for position, current_security in enumerate(sorted(security)):
            point, type = current_security
            count += type
            # print(count, point, type)
            # print(point, type, count)
            if count == 0 and position != len(security)-1:
                result.append('Wrong Answer')
                break
            if count > 2:
                result.append('Wrong Answer')
                break
        else:
            result.append('Accepted')
        # print(count)
    return '\n'.join(result)


with open('input.txt') as file:
    lines = file.readlines()
    k = int(lines[0])
    full_security = []
    for line in lines[1:]:
        security = []
        for t1 in line.split()[1::2]:
            security.append((int(t1), 1))
        for t2 in line.split()[2::2]:
            security.append((int(t2), -1))
        full_security.append(security)
    # print(full_security)

with open('output.txt', 'w') as file:
    file.write(check_security(full_security))
