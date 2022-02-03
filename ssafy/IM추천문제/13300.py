student_num, k = map(int, input().split())
student = []

for i in range(student_num):
    student.append(list(map(int, input().split())))
res = []
a = 0

print(student)
for i in range(len(student)):
    if student[i][0] == 0:
        for y in range(1,7):
            a += student.count([0, y])
            # print(0, y,  student.count([0, y]))

    elif student[i][1] == 1:
        for y in range(1,7):
            # print(1, y,  student.count([1, y]))
            a += student.count([0, y])
