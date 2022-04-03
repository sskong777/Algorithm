import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    arr = [[0]*(N+1) for _ in range(N+1)]

    arr[N//2+1][N//2],arr[N//2][N//2+1] = 1,1
    arr[N//2][N//2],arr[N//2+1][N//2+1] = 2,2

    s = []
    for m in range(M):
        si,sj,d = map(int,input().split())
        arr[si][sj] = d
        for di,dj in ((1,1),(1,-1),(-1,1),(-1,-1),(0,1),(0,-1),(1,0),(-1,0)):

            for k in range(1, N):
                ni,nj = si+di*k, sj+dj*k
                # 범위 내
                if 1<=ni<=N and 1<=nj<=N:
                    if arr[ni][nj] ==0 :
                        break
                    elif arr[ni][nj] == d:
                        for ci,cj in s:
                            arr[ci][cj] = d
                        break
                    else:
                        s.append((ni,nj))
                # 범위 밖
                else:
                    break

    b_cnt,w_cnt = 0,0
    for lst in arr:
        b_cnt += lst.count(1)
        w_cnt += lst.count(2)

    print(f'#{tc} {b_cnt} {w_cnt}')