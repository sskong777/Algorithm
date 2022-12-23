from collections import deque

def bfs(start):
    q = deque([start])

    count = 1
    while q:
        ci,cj = q.popleft()

        for di,dj in ((-1,0),(1,0),(0,1),(0,-1)):
            ni,nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<M and not visited[ni][nj] and arr[ni][nj] == 0:
                q.append((ni,nj))
                visited[ni][nj] = 1
                count += 1

    return count


def build_3walls(*walls):
    for wall in walls:
        wi,wj = empty[wall][0], empty[wall][1]
        arr[wi][wj] = 1

def break_3walls(*walls):
    for wall in walls:
        wi,wj = empty[wall][0], empty[wall][1]
        arr[wi][wj] = 0

def infection():
    cnt = 0
    for i,j in virus:
        visited[i][j] = 1
        cnt += bfs((i,j))
    return cnt

N,M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]

virus = []
empty = []
wall_cnt = 0
safe_cnt = 0

for i in range(N):
    for j in range(M):
        if arr[i][j] == 2:
            virus.append((i,j))
        elif arr[i][j] == 0:
            empty.append((i,j))
        else:
            wall_cnt += 1


for w1 in range(len(empty)):
    for w2 in range(w1+1, len(empty)):
        for w3 in range(w2+1, len(empty)):
            build_3walls(w1,w2,w3)

            visited = [[0] * M for _ in range(N)]
            sum_area = N*M
            infection_cnt = infection()
            cnt = sum_area - infection_cnt - 3 - wall_cnt

            safe_cnt = max(safe_cnt,cnt)

            break_3walls(w1,w2,w3)

print(safe_cnt)
