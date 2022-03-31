from collections import deque
def bfs(i,j):
    v[i][j] = 1

    for move in range(1,N):
        for di,dj in ((1,0),(0,1),(-1,0),(0,-1)):
            ni,nj = i+di*move, j+dj*move
            if 0<= ni <N and 0<= nj <N and v[ni][nj] == 0:
                    v[ni][nj] = 1

N = 4
v = [[0] * N for _ in range(N)]

bfs(2,2)
print(v)