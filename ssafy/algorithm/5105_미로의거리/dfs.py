import sys
sys.stdin = open('input.txt', 'r')

def fstart(N):
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                return i, j
    return -1, -1

def dfs(i,j,N,c):       # c: 지나온 칸 수
    global minV
    if maze[i][j] == 3:
        if minV > c:
            minV = c
    else:
        maze[i][j] = 1  # 출발지 막기
        for di, dj in [[0,1], [1,0], [0,-1], [-1,0]]:    # i,j에 인접한 칸에 대해
            ni, nj = i + di, j + dj
            if 0<= ni <N and 0<= nj <N and maze[ni][nj] != 1:
                dfs(ni, nj, N, c+1)
        maze[i][j] = 0


T = int(input())
for tc in range(1,T+1):
    N  = int(input())
    maze = [list(map(int,input())) for _ in range(N)]
    sti, stj = fstart(N)

    minV = 10000  # 나올 수 있는 최대값으로 설정

    dfs(sti, stj, N, 0)
    if minV == 10000:
        minV = 1

    print("#{} {}".format(tc, minV-1))
