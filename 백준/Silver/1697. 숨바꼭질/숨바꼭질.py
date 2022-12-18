from collections import deque


def bfs(N):
    q = deque()
    q.append(N)
    v[N] = 1

    while q:
        next = q.popleft()

        if next == K:
            return v[next]
        for i in next-1, next+1, next*2:
            if 0<=i<100001 and v[i]==0:
                q.append(i)
                v[i] = v[next] + 1


N,K = map(int,input().split())

# arr = [0]*100001
v = [0]*100001
# arr[N] = 1
# arr[K] = 2

res = bfs(N)
print(res-1)