# deque 사용
from collections import deque
N = int(input())

q = deque([i for i in range(1,N+1)])

while len(q) != 1:
    q.popleft()
    a = q.popleft()
    q.append(a)

print(q[0])