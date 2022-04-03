# 파이써닉한 코드

import sys
from collections import deque
sys.stdin = open('input.txt', 'r')

def bfs(N,M,si,sj,L):
    q = deque()
    v = [[0]*M for _ in range(N)]
    q.append((si,sj))
    v[si][sj] = 1
    cnt = 1

    while q:
        ci,cj = q.popleft()
        # 종료조건
        if v[ci][cj] == L:
            return cnt

        for k in range(4):
            ni,nj = ci+di[k], cj+dj[k]
            if 0<=ni<N and 0<= nj <M and v[ni][nj] == 0 and\
                k in pipe[arr[ci][cj]] and opp[k] in pipe[arr[ni][nj]]:
                q.append((ni,nj))
                v[ni][nj] = v[ci][cj] + 1
                cnt += 1
    return cnt


pipe = [
   #상 하 좌 우
    [],
    [0,1,2,3],
    [0,1],
    [2,3],
    [0,3],
    [1,3],
    [1,2],
    [0,2]
]

di,dj = (-1,1,0,0), (0,0,-1,1)

# 연결될 파이프를 확인할 opposit배열
opp = [1,0,3,2]


T = int(input())
for tc in range(1,T+1):
    # N,M(세로,가로) / R,C(맨홀위치) / L : 탈출 후 소요시간
    N,M,R,C,L = map(int,input().split())
    # 지도 입력받기
    arr = [list(map(int,input().split())) for _ in range(N)]
    ans = bfs(N,M,R,C,L)
    print(f'#{tc} {ans}')