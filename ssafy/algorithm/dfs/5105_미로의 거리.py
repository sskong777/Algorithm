# # 5106 미로의 거리

# 출발점 찾기
def fstart(N):
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                return i, j
    return -1, -1

def dfs(i,j,N,c):   # c:지나온 칸수
    global minV
    if maze[i][j] == 3: # 목적지에 도착하면 기존의 최소거리와 비교
        if minV > c:
            minV = c
    else:
        maze[i][j] = 1  # 지나온 경로 1로 막기.
        for di, dj in [[0,1], [1,0], [-1,0], [0,-1]]:
            ni, nj = i+di, j+dj
            if 0<= ni<N and 0<=nj<N and maze[ni][nj] != 1:
                dfs(ni,nj,N,c+1)
        maze[i][j] = 0





T = int(input())
for tc in range(1,T+1):
    N  = int(input())
    maze = [list(map(int,input())) for _ in range(N)]
    sti, stj = fstart(N)

    minV = 10000
    dfs(sti, stj, N, 0)
    if minV == 10000:
        minV = 1
    print(f'#{tc} {minV - 1}')