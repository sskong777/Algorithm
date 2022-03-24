# 시간 초과
n = int(input())
q = [i for i in range(1,n+1)]

# q = arr
while len(q) != 1:
    q.pop(0)
    a = q.pop(0)
    q.append(a)

print(*q)