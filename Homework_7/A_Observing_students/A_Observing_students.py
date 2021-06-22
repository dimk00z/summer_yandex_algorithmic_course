def do_observing(n, m, b_e):
    students = {}
    # print(students)
    for teacher in b_e:
        for teacher_look in range(teacher[0], teacher[1]+1):
            if teacher_look not in students:
                students[teacher_look] = True

    # print(students)
    result = n - len(students)
    return str(result)
    # return str(students.count(None))


with open('input.txt') as file:
    lines = file.readlines()
    # n -students, m - teachers
    n, m = map(int, lines[0].split())
    # b_e - teachers
    b_e = sorted([tuple(map(int, line.split())) for line in lines[1:]])


with open('output.txt', 'w') as file:
    file.write(do_observing(n, m, b_e))
