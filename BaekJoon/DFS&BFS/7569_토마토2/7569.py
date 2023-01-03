import sys
sys.stdin = open('input.txt', 'r')

from collections import deque

def find_start(arr):
    starts = []
    for h in range(H):
        for n in range(N):
            for m in range(M):
                if arr[h][n][m] == 1:
                    starts.append((h,n,m))
    return starts



def bfs(starts):
    q = deque(starts)

    while q:
        ch,ci,cj = q.popleft()
        for di,dj,dh in ((-1,0,0),(1,0,0),(0,1,0),(0,-1,0),(0,0,-1),(0,0,1)):
            ni,nj,nh = ci+di, cj+dj, ch+dh
            if 0<=ni<N and 0<=nj<M and 0<=nh<H and arr[nh][ni][nj]==0:
                q.append((nh,ni,nj))
                arr[nh][ni][nj] = arr[ch][ci][cj] + 1


M, N, H = map(int,input().split())
arr = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

starts = find_start(arr)
bfs(starts)

flag = 0
result = -2
for i in range(H):
    for j in range(N):
        for k in range(N):
            # 높이, x,y 순서
            if arr[i][j][k] == 0:
                flag = 1
                # 높이, x,y 순서
            result = max(result,arr[i][j][k])
if flag == 1:
    print(-1)
elif result == -1:
    print(0)
else:
    print(result-1)