import sys
sys.stdin = open('input.txt', 'r')

N, M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]

cctv = []
for i in range(N):
    for j in range(M):
        if arr[i][j] in [1,2,3,4,5]:
            cctv.append((i, j, arr[i][j]))

visited = [[0]*(M+1) for _ in range(N+1)]

N, M = map(int, input().split())
ans=M*N
office=[]
cctv=[]
for i in range(N):
    line=list(map(int, input().split()))
    office.append(line)
    for j in range(M):
        if line[j]!=0 and line[j]!=6: cctv.append([i,j,line[j]]); ans-=1
        elif line[j]==6: ans-=1

#남-북-동-서
dx=[1,-1,0,0]
dy=[0,0,1,-1]
direction=[
    [],
    [[0],[1],[2],[3]],
    [[0,1],[2,3]],
    [[1,2],[2,0],[0,3],[3,1]],
    [[0,1,2],[0,1,3],[0,2,3],[1,2,3]],
    [[0,1,2,3]]
    ]

def watch(x,y, dir, temp):
    count=0
    for d in dir:
        nx=x
        ny=y
        while True:
            nx+=dx[d]
            ny+=dy[d]
            if 0<=nx<N and 0<=ny<M and temp[nx][ny]!=6:
                if temp[nx][ny]==0: temp[nx][ny]=-1; count+=1
            else: break
    return count

MIN=M*N
def dfs(office, depth):
    global ans
    global MIN
    temp = [o[:] for o in office]
    if depth==len(cctv):
        MIN=min(MIN, ans)
        return
    x, y, type=cctv[depth]
    for dir in direction[type]:
        a=watch(x,y,dir,temp)
        ans-=a
        dfs(temp, depth+1)
        ans+=a
        temp = [o[:] for o in office]

dfs(office, 0)
print(MIN)
