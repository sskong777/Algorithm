
from collections import deque

# N :도시의 개수
# M : 도로의 개수
# K : 거리 정보
# X : 출발 도시 번호



N,M,K,X = map(int,input().split())
# adj = [[0]*(N+1) for _ in range(N+1)]
graph = [[] for _ in range(N+1)]
v = [0] * (N+1)
for i in range(M):
    A ,B = map(int,input().split())
    # adj[A][B] = 1
    graph[A].append(B)

q = deque()
sol = []
q.append(X)
## 이 부분에서 헤맸음
v[X] = 1
while q:
    c = q.popleft()
    for j in graph[c]:
        if v[j] == 0:
            nc = j
            v[nc] = v[c] + 1
            q.append(nc)

check = False
for i in range(1,N+1):
    # ** v[i] -1을 해줘야한다.
    if v[i]-1 == K:
        print(i)
        check = True
if check == False:
    print(-1)