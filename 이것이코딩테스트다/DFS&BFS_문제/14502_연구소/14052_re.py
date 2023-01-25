import sys
sys.stdin = open('input.txt', 'r')

# 조합 combination 사용
# 시작점 여러개 bfs
from itertools import combinations
from collections import deque
def bfs(virus):
    q = deque(virus)
    for i,j in virus:
        visited[i][j] = 1
    cnt = len(virus)

    while q:
        ci,cj = q.popleft()
        for di,dj in ((-1,0),(1,0),(0,1),(0,-1)):
            ni,nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<M  and arr[ni][nj] == 0 and not visited[ni][nj]:
                q.append((ni,nj))
                visited[ni][nj] = 1
                cnt += 1
    return cnt


def build_wall(w_l):
    for w in w_l:
        wi,wj = w
        arr[wi][wj] = 1


def break_wall(w_l):
    for w in w_l:
        wi,wj = w
        arr[wi][wj] = 0

N,M = map(int,input().split())

# 지도 입력받기
arr = [(list(map(int,input().split()))) for _ in range(N)]
virus = []
empty = []
walls = 0
safe = 0

for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            empty.append((i,j))
        elif arr[i][j] == 2:
            virus.append((i,j))
        else:
            walls += 1

wall_list = combinations(empty,3)

cnt = 0
for w_l in wall_list:
    build_wall(w_l)

    visited = [[0]*M for _ in range(N)]

    cnt = bfs(virus)

    cur_safe = N * M - walls - 3 - cnt
    safe = max(cur_safe, safe)
    break_wall(w_l)

print(safe)