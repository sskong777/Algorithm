import sys
sys.stdin = open('input.txt', 'r')

def fstart(N):
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                return i, j
    return -1, -1

def bfs(i,j,N):
    visited = [[0]*N for _ in range(N)] # 미로의 크기 만큼 생성
    queue = []  #큐 생성
    queue.append((i,j))     # 시작점 인큐
    visited[i][j] = 1       # 시작점 방문표시
    while queue:
        i,j = queue.pop(0)  # 디큐
        if maze[i][j] == 3:      # visit(t)
            return visited[i][j] -2     #출발 도착 칸 제외

        for di, dj in [[0,1], [1,0], [0,-1], [-1,0]]:    # i,j에 인접한 칸에 대해
            ni, nj = i + di, j + dj
            if 0<= ni <N and 0<= nj <N and maze[ni][nj] != 1 and  visited[ni][nj] == 0:
                queue.append((ni,nj))
                visited[ni][nj] = visited[i][j] + 1
    # 도착지를 찾지 못한경우
    return 0


T = int(input())
for tc in range(1,T+1):
    N  = int(input())
    maze = [list(map(int,input())) for _ in range(N)]

    sti, stj = fstart(N)
    ans = bfs(sti, stj, N)
    print("#{} {}".format(tc,ans))


    # print(sti, stj)
    # ans = bfs()
