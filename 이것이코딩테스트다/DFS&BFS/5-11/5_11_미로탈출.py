import sys
from pprint import pprint
sys.stdin = open('input.txt', 'r')

def bfs(i,j,N,M):
    visited = [[0] * M for _ in range(N)]
    q = []
    # i,j = 0,0   # 시작점
    q.append((i,j))   # 시작점 인큐
    visited[i][j] = 1   #시작점 방문처리

    while q:    # 큐가 비어있을 때 까지
        i,j = q.pop(0)
        if i == N-1 and j == M-1:
            return visited[i][j]
        for di,dj in [[1,0],[0,1],[-1,0],[0,-1]]:
            ni,nj = i+di, j+dj
            # ni와 nj가 범위 안에 있고, maze의 ni,nj가 괴물이 없는부분이며 방문이 되지 않은 곳이면
            if  0<=ni<N and 0<=nj<M and maze[ni][nj] != 0 and visited[ni][nj] == 0:
                q.append((ni,nj))
                visited[ni][nj] = visited[i][j] + 1
    return

N, M = map(int,input().split())
maze = [list(map(int,input())) for _ in range(N)]

ans = bfs(0,0,N,M)
print(ans)
# pprint(maze)
# pprint(visited)

