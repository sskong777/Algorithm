import sys
sys.stdin = open('input.txt', 'r')

# NxN 크기의 시험관이 있다. 시험관은 1x1 크기의 칸으로 나누어지며, 특정한 위치에는 바이러스가 존재할 수 있다. 모든 바이러스는 1번부터 K번까지의 바이러스 종류 중 하나에 속한다.
#
# 시험관에 존재하는 모든 바이러스는 1초마다 상, 하, 좌, 우의 방향으로 증식해 나간다. 단, 매 초마다 번호가 낮은 종류의 바이러스부터 먼저 증식한다. 또한 증식 과정에서 특정한 칸에 이미 어떠한 바이러스가 존재한다면, 그 곳에는 다른 바이러스가 들어갈 수 없다.
#
# 시험관의 크기와 바이러스의 위치 정보가 주어졌을 때, S초가 지난 후에 (X,Y)에 존재하는 바이러스의 종류를 출력하는 프로그램을 작성하시오. 만약 S초가 지난 후에 해당 위치에 바이러스가 존재하지 않는다면, 0을 출력한다. 이 때 X와 Y는 각각 행과 열의 위치를 의미하며, 시험관의 가장 왼쪽 위에 해당하는 곳은 (1,1)에 해당한다.
#
# 예를 들어 다음과 같이 3x3 크기의 시험관이 있다고 하자. 서로 다른 1번, 2번, 3번 바이러스가 각각 (1,1), (1,3), (3,1)에 위치해 있다. 이 때 2초가 지난 뒤에 (3,2)에 존재하는 바이러스의 종류를 계산해보자.

from collections import deque

def bfs(start):
    q = deque(start)
    for s,i,j in start:
        visited[i][j] = 1

    while q:
        v, ci, cj = q.popleft()
        if visited[ci][cj]-1 == S:
            return

        for di,dj in ((-1,0),(1,0),(0,1),(0,-1)):
            ni,nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<N and not visited[ni][nj] and arr[ni][nj] == 0:
                q.append((v,ni,nj))
                visited[ni][nj] = visited[ci][cj] + 1
                arr[ni][nj] = v

N, K = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
S, X, Y = map(int,input().split())

start = []
for i in range(N):
    for j in range(N):
        if arr[i][j] != 0:
            start.append((arr[i][j], i, j))

start.sort()
visited = [[0]*N for _ in range(N)]
ans = bfs(start)
print(arr[X-1][Y-1])
