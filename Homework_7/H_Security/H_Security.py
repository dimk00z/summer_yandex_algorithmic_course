def check_security(full_security):
    result = []
    for security in full_security:
        count = 0
        security.sort()
        print()
        print(security)
        last_count = 0
        if len(security) == 2 and security[0][0] != 0 and security[1][0] != 10000:
            result.append('Wrong Answer')
            continue
        if security[-1][0] != 10000 or security[0][0] != 0:
            result.append('Wrong Answer')
            continue
        for position, current_security in enumerate(security):
            point, type = current_security
            count += type
            print(position, count, point, type)
            # print(point, type, count)
            if count == 0 and position != len(security)-1:
                if current_security[0] != security[position+1][0]:
                    # print(current_security, security[position+1])
                    result.append('Wrong Answer')
                    break
            print('last_count ', last_count, 'count ',
                  count, last_count > count, count-1 > 0)
            # print('count ', count)
            if last_count > count and count-1 > 0:
                print('Blaaaaaaaaaaaa')
                result.append('Wrong Answer')
                break
            if count > 2:
                result.append('Wrong Answer')
                break

            last_count = count
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
