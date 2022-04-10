# 이코테 ch6의 아이스크림 문제에서 아이디어를 얻었다.
# visited를 공용으로 사용하며, 반복문으로 배열을 순회하면서 visited배열을 확인하며 bfs를 실행한다.
import sys
sys.stdin = open('input.txt', 'r')

def bfs(si,sj):
    q = []
    # move에 인구이동이 일어난 좌표를 담아준다.
    move = [(si,sj)]
    # ssum = arr[si][sj]
    q.append((si,sj))
    v[si][sj] = 1

    while q:
        ci,cj = q.pop(0)
        #
        for di,dj in ((1,0),(0,1),(-1,0),(0,-1)):
            ni,nj = ci+di,cj+dj
            if 0<=ni<N and 0<=nj<N and v[ni][nj]==0\
                and L<=abs(arr[ci][cj]-arr[ni][nj])<=R:
                v[ni][nj] = 1
                q.append((ni,nj))
                move.append((ni,nj))
                # ssum += arr[ni][nj]
    # 인구이동이 일어난 좌표와 좌표의 갯수를 반환해준다
    # 만약 인구 이동이 일어나지 않았다면, move에는 시작점 좌표만 들어있다.
    return move, len(move)

def population_movement(move):
    global arr
    ssum = 0
    for x, y in move:
        ssum += arr[x][y]
    for x, y in move:
        arr[x][y] = ssum // len(move)


N,L,R = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]

res = 0
# 인구이동이 일어나지 않을 때 까지 반복
while True:
    # 인구 이동이 일어날 때 마다 visited배열을 초기화 해주어야한다.
    v = [[0] * N for _ in range(N)]
    flag = False
    for si in range(N):
        for sj in range(N):
            if v[si][sj]==0:
                move, move_cnt = bfs(si,sj)
                # move_cont가 1보다 크면 인구 이동이 가능으므로
                if move_cnt > 1:
                    flag = True
                    # flag 변수를 True로 바꿔 while문을 계속해서 돌게 한 뒤
                    # 인구이동을 시켜준다.
                    population_movement(move)

    # 인구 이동이 일어나지 않았으므로 break로 while문 탈출
    if not flag:
        break
    # while문을 한바퀴 돌 때 마다 인구이동의 횟수가 하나씩 증가한다.
    res += 1

print(res)