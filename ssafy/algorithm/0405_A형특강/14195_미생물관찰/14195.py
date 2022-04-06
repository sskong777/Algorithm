import sys
sys.stdin = open('input.txt', 'r')

def bfs_A(si,sj,lst):
    global cnt_A
    q = []
    q.append((si,sj))
    v[si][sj] = 1

    while q:
        ci,cj = q.pop(0)

        for di,dj in ((1,0),(0,1),(-1,0),(0,-1)):
            ni,nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<M and v[ni][nj] == 0 and arr[ni][nj] =='A':
                q.append((ni,nj))
                v[ni][nj] = v[ci][cj] + 1

    return v

T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    arr = [list(input()) for _ in range(N)]
    print(arr)
    v = [[0]*M for _ in range(N)]


    cnt_A = 0
    cnt_B = 0
    mmax = 0
    # for si in range(N):
    #     for sj in range(M):
    #         if arr[si][sj] =='A':
    #             bfs_A(si,sj,[])
    #             cnt_A += 1
    #         if arr[si][sj] =='B':
    #             pass
    #         # mmax = max()
    ans = bfs_A(0,0,[])
    print(ans)