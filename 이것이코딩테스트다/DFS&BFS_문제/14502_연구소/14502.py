import sys
from collections import deque
sys.stdin = open('input.txt', 'r')

# 3중 for문 사용
# 2중 for문 시작점 여러개인 bfs

def bfs(start):
    global N,M
    q = deque([start])
    cnt  = 1
    while q:
        si,sj = q.popleft()
        for di,dj in ((1,0),(-1,0),(0,-1),(0,1)):
            ni, nj  = si+di, sj+dj
            if 0<=ni<N and 0<=nj<M and arr[ni][nj]==0 and not visited[ni][nj]:
                visited[ni][nj] = 1
                q.append((ni,nj))
                cnt += 1
    return cnt

def infection():
    cnt = 0
    for i,j in virus:
        visited[i][j] = 1
        cnt += bfs((i,j))
    return cnt

def build_wall(*ws):
    for w in ws:
        i,j = empty[w][0],empty[w][1]
        arr[i][j] = 1

def break_wall(*ws):
    for w in ws:
        i,j = empty[w][0],empty[w][1]
        arr[i][j] = 0



N,M = map(int,input().split())

# 지도 입력받기
arr = []
virus = []
empty = []
walls = 0
safe = 0
for i in range(N):
    arr.append(list(map(int,input().split())))

# 바이러스 위치 표시
for i in range(N):
    for j in range(M):
        if arr[i][j] == 2:
            virus.append((i,j))
        elif arr[i][j] == 1:
            walls += 1
        else:
            empty.append((i,j))

for w1 in range(len(empty)):
    for w2 in range(w1+1,len(empty)):
        for w3 in range(w2+1,len(empty)):
            # 벽 3개 세우기
            build_wall(w1,w2,w3)

            # bfs로 바이러스 퍼트리기
            visited = [[0]*M for _ in range(N)]
            cur_safe = N*M - walls - 3 - infection()
            safe = max(cur_safe,safe)

            break_wall(w1,w2,w3)
print(safe)
