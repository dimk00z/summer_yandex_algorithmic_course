from statistics import median


def find_median_sorted_arrays(arr1, arr2):
    arr = arr1 + arr2
    arr.sort()
    n = len(arr)

    # If length of array is even
    if n % 2 == 0:
        z = n // 2
        e = arr[z]
        q = arr[z - 1]
        ans = (e + q) / 2
        return ans

    # If length of array is odd
    else:
        z = n // 2
        ans = arr[z]
        return ans


def calculate_medians(numbers_lists):
    print(find_median_sorted_arrays(numbers_lists[0], numbers_lists[1]))
    print(median(numbers_lists[0] + numbers_lists[2]))
    return 'dd'


with open('input.txt') as file:
    numbers_lists = [list(map(int, line.split())) for line in file.readlines()]

with open('output.txt', 'w') as file:
    file.write(str(calculate_medians(numbers_lists)))
