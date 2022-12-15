
from collections import deque
def bfs(starts):
    q = deque(starts)

    # for start in starts:
    #     si,sj = start
    #     # v[si][sj] = 1

    while q:
        ci,cj = q.popleft()

        for di,dj in ((1,0),(0,1),(-1,0),(0,-1)):
            ni,nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<M and arr[ni][nj]==0:
                q.append((ni,nj))
                arr[ni][nj] = arr[ci][cj] + 1
                # v[ni][nj] = v[ci][cj] + 1


def find_start():
    lst = []
    for i in range(N):
        for j in range(M):
            if arr[i][j]==1:
                lst.append((i,j))
    return lst


M,N = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
v = [[0] * M for _ in range(N)]
res = 0
# for i in range(N):
#     if 0 not in arr[i]:
#         print(0)
#         exit(0)

starts = find_start()
bfs(starts)
# print(arr)
# print(v)
flag = True
for i in arr:
    for j in i:
        if j==0:
            print(-1)
            exit(0)
    res = max(res,max(i))
print(res-1)
