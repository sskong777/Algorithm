# 메모리 초과
from collections import deque

# N :도시의 개수
# M : 도로의 개수
# K : 거리 정보
# X : 출발 도시 번호

def bfs(X,K):
    q = deque()
    sol = []

    q.append(X)
    ## 이 부분에서 헤맸음
    v[X] = 0

    while q:
        c = q.popleft()
        if v[c] == K:
            sol.append(c)

        for j in range(1,N+1):
            if adj[c][j] == 1 and v[j] == 0:
                nc = j
                v[nc] = v[c] + 1
                q.append(nc)
    return sol

N,M,K,X = map(int,input().split())
adj = [[0]*(N+1) for _ in range(N+1)]
v = [0] * (N+1)
for i in range(M):
    A ,B = map(int,input().split())
    adj[A][B] = 1

sol = bfs(X,K)
if len(sol) == 0:
    print(-1)
else:
    for i in sol:
        print(i)