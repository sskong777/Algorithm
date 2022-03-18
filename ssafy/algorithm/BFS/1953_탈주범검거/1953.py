import sys
sys.stdin = open('input.txt', 'r')

# pipe 배열 만들기 상 하 좌 우
pipe = [[0,0,0,0], [1,1,1,1], [1,1,0,0], [0,0,1,1], [1,0,0,1], [0,1,0,1], [0,1,1,0], [1,0,1,0]]

# di,dj  상 하 좌 우 만들기
di, dj = (-1,1,0,0), (0,0,-1,1)

# 방향 배열 상 하 좌 우 만들기
opp= [1,0,3,2]


def bfs(N,M,si,sj,L):
    q = []
    v = [[0]*M for _ in range(N)]

    q.append((si,sj))
    v[si][sj] = 1
    cnt = 1

    while q:
        ci,cj = q.pop(0)
        if v[ci][cj] == L:
            return cnt

        # 4개 방향 돌리기
        for k in range(4):
            ni,nj = ci+di[k], cj+dj[k]
            if 0<=ni<N and 0<=nj<M and v[ni][nj] == 0 \
                and pipe[arr[ci][cj]][k] and pipe[arr[ni][nj]][opp[k]]:  # 현재(arr[ci][cj]번) 파이프의 k번째 방향이 있고,
                q.append((ni,nj))                                        # 다음(pipe[arr[ni][nj]]) 파이프가 현재 파이프와 연결이 되어있으면
                v[ni][nj] = v[ci][cj] + 1
                cnt += 1
    return cnt

T = int(input())
for tc in range(1,T+1):
    N, M, R, C, L = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    # print(arr)

    ans = bfs(N,M,R,C,L)
    print(f'#{tc} {ans}')