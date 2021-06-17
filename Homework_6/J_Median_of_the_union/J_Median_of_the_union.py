from statistics import median


def median(arr, n):
    if n % 2 == 0:
        return (arr[int(n / 2)] +
                arr[int(n / 2) - 1]) / 2
    else:
        return arr[int(n/2)]


def get_median(arr1, arr2, n):
    if n == 2:
        return (max(arr1[0], arr2[0]) +
                min(arr1[1], arr2[1])) / 2
    else:
        m1 = median(arr1, n)
        m2 = median(arr2, n)
        if m1 > m2:
            if n % 2 == 0:
                return get_median(arr1[:int(n / 2) + 1],
                                  arr2[int(n / 2) - 1:], int(n / 2) + 1)
            else:
                return get_median(arr1[:int(n / 2) + 1],
                                  arr2[int(n / 2):], int(n / 2) + 1)
        else:
            if n % 2 == 0:
                return get_median(arr1[int(n / 2 - 1):],
                                  arr2[:int(n / 2 + 1)], int(n / 2) + 1)
            else:
                return get_median(arr1[int(n / 2):],
                                  arr2[0:int(n / 2) + 1], int(n / 2) + 1)


with open('input.txt') as file:
    lines = file.readlines()
    n, l = list(map(int, lines[0].split()))
    arr = [list(map(int, line.split()))
           for line in lines[1:]]
print(arr)
test_arr = arr[1] + arr[2]
test_arr.sort()
print(test_arr[l-1])
print(int(get_median(arr[0], arr[1], l)))
print(median(test_arr, len(test_arr)))
# with open('output.txt', 'w') as file:
#     file.write(str(calculate_medians(numbers_lists, n, l)))
