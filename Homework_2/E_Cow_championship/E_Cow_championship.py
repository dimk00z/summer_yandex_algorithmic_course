

def fetch_Vasya_position(champions_number, results):
    if champions_number < 3:
        return 0
    max_result = max(results)
    max_position = results.index(max_result)
    if ((champions_number-1)-max_position) < 2:
        return 0
    Vasya_result = None
    for position, value in enumerate(
            results[max_position+1:champions_number-1]):
        if (value % 10 == 5):
            if results[
                max_position+position+1] > results[
                    max_position+position+2]:
                if Vasya_result is None:
                    Vasya_result = value
                    continue
                if Vasya_result < value:
                    Vasya_result = value
    if Vasya_result:
        results = sorted(results,  reverse=True)
        return results.index(Vasya_result)+1
    return 0


with open('input.txt') as file:
    lines = file.readlines()
    champions_number = int(lines[0])
    results = list(map(int, lines[1].split()))

with open('output.txt', 'w') as file:
    file.write(str(fetch_Vasya_position(champions_number, results)))
