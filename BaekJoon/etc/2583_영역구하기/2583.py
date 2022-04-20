import sys
sys.stdin = open('input.txt')

def dfs(si,sj):
    stack = []
    stack.append((si,sj))
    v[si][sj] = 1
    move = 1
    while stack:
        ci,cj = stack.pop()
        for di,dj in ((1,0),(0,1),(-1,0),(0,-1)):
            ni,nj = ci+di, cj+dj
            if 0<=ni<M and 0<=nj<N and v[ni][nj]==0 and arr[ni][nj]==1:
                stack.append((ni,nj))
                v[ni][nj] = 1
                move += 1
    return move


M,N,K = map(int,input().split())
arr = [[1]*N for _ in range(M)]

for k in range(K):
    x1,y1,x2,y2 = map(int,input().split())

    for y in range(y1, y2):
        for x in range(x1, x2):
            arr[y][x] = 0

v = [[0]*N for _ in range(M)]
moves = []
cnt = 0
for si in range(M):
    for sj in range(N):
        if not v[si][sj] and arr[si][sj] == 1:
            move = dfs(si,sj)
            cnt += 1
            moves.append(move)
moves.sort()

print(cnt)
print(*moves)