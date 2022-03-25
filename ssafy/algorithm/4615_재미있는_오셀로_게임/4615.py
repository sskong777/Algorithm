import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())

    # 1부터 접근하기 편하기 위해
    arr = [[0]*(N+1) for _ in range(N+1)]

    # 초기 오셀로판 세팅
    arr[N // 2][N // 2] = arr[N // 2 + 1][N // 2 + 1] = 2
    arr[N // 2 + 1][N // 2] = arr[N // 2][N // 2 + 1] = 1

    s = []
    for i in range(M):
        # 좌표, 돌 색깔
        sj,si,d = map(int,input().split())
        arr[si][sj] = d
        for di,dj in ((-1,-1),(-1,0),(-1,1),(1,0),(1,-1),(1,1),(0,1),(0,-1)):
            for k in range(1,N):
                ni,nj = si+di*k, sj+dj*k
                if 1<=ni<=N and 1<=nj<=N:
                    if arr[ni][nj] == 0:
                        break
                    elif arr[ni][nj] == d:
                        for ci,cj in s:
                            arr[ci][cj] = d
                    else:
                        s.append((ni,nj))
                else:
                    break

    bcnt = wcnt = 0
    for lst in arr:
        bcnt += lst.count(1)
        wcnt += lst.count(2)
    print(f'#{tc} {bcnt} {wcnt}')