students = ["John", "Mark", "Trump", "Biden"]


def divide_students(x):
    group = [[], []]
    for idx, student in enumerate(x):
        if idx % 2 == 0:
            group[0].append(student)
        else:
            group[1].append(student)
    print(group)

divide_students(students)
