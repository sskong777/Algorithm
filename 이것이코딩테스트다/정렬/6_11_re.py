
N = int(input())

array = []
for i in range(N):
    name, score = input().split()
    array.append((name,int(score)))

array.sort(key=lambda student: student[1])

for i in range(N):
    print(array[i][0], end=' ')