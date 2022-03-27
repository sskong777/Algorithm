from collections import deque



def bfs(S):
    q = deque(data)
    vir,x,y = data[0]
    v = [[0]* N for _ in range(N)]
    v[x][y] = 0
    while q:
        num,x,y = q.popleft()
        if v[x][y] == S:
            return

        for dx,dy in ((1,0),(0,1),(-1,0),(0,-1)):
            nx,ny = x+dx, y+dy
            if 0<=nx<N and 0<=ny<N and arr[nx][ny]==0:
                arr[nx][ny] = num
                q.append((num,nx,ny))
                v[nx][ny] = v[x][y] + 1


N,K = map(int,input().split())
# arr = [['']*(N+1)]+[['']+list(map(int,input().split())) for _ in range(N)]
arr = [list(map(int,input().split())) for _ in range(N)]
S,X,Y = map(int,input().split())
# v = [[0]*N for _ in range(N)]

data = []
# 시험관에 바이러스가 있으면 바이러스 번호와 좌표 넣어주기
for i in range(N):
    for j in range(N):
        if arr[i][j]:
            data.append((arr[i][j],i,j))

# 바이러스 번호를 기준으로 오름차순 정렬
data.sort()


bfs(S)
# print(arr)

if arr[X-1][Y-1]:
    print(arr[X-1][Y-1])
else:
    print(0)
