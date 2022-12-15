import sys
sys.stdin = open('input.txt', 'r')

def bfs(si,sj):
    q = []
    q.append((si,sj))
    visited[si][sj] = 1

    apart = [(si,sj)]
    while q:
        ci,cj = q.pop(0)

        for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni,nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<N and visited[ni][nj] == 0 and arr[ni][nj] == 1:
                q.append((ni, nj))
                visited[ni][nj] = visited[ci][cj] + 1
                apart.append((ni,nj))
    return apart



N = int(input())
arr = [list(map(int,input())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]

complex = 0
aparts_cnt = []

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1 and  visited[i][j] == 0:
            aparts = bfs(i,j)
            complex +=1
            aparts_cnt.append(len(aparts))

print(complex)
aparts_cnt.sort()
for ans in aparts_cnt:
    print(ans)
# print(aparts_cnt)