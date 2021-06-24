# Thx https://github.com/Yankovsky/yandex-algos-training/blob/master/hw7/c.py

from heapq import heappop, heappush

STUDENT_START = -1
STUDENT_END = 1


def calculate_variants(n, d, x):

    line_with_distance = []
    max_student = 0
    for student in x:
        max_student = max(max_student, student)
        line_with_distance.append(
            (student, STUDENT_START))
        line_with_distance.append(
            (student + d, STUDENT_END))
    line_with_distance.sort()
    # print(line_with_distance)

    final_students = {}
    heap = list(range(1, n + 1))
    max_exam_number = 0

    for point in line_with_distance:
        if point[1] == STUDENT_START:
            # print(heap)
            next_exam_number = heappop(heap)
            max_exam_number = max(max_exam_number, next_exam_number)
            final_students[point[0]] = next_exam_number

        elif point[1] == STUDENT_END:
            student_exam_number = final_students[point[0] - d]
            heappush(heap, student_exam_number)

    result = []
    result.append(str(max_exam_number))
    result.append(
        ' '.join(map(str, [final_students[student] for student in x])))
    return '\n'.join(result)


with open('input.txt') as file:
    lines = file.readlines()
    # n -students, d - distance between students
    n, d = map(int, lines[0].split())
    # x - students position
    x = list(map(int, lines[1].split()))


with open('output.txt', 'w') as file:
    file.write(calculate_variants(n, d, x))
