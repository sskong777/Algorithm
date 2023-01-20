import sys
sys.stdin = open('input.txt', 'r')

#  우 하 좌 상
dx = [0,1,0,-1]
dy = [1,0,-1,0]

N = int(input())
K = int(input())
arr = [[0] * (N+1) for _ in range(N+1)]

# 사과 위치  => 1
for k in range(K):
    r,c = map(int,input().split())
    arr[r][c] = 1       # 과일 위치에 1 남기기

# 방향 정보
L = int(input())
turn = []
for l in range(L):
    x,c = input().split()
    turn.append((int(x),c))


def bam_turn(direction,c):
    if c == 'L':
        direction = (direction-1) % 4   # 상 좌 하 우
    else:
        direction = (direction+1) % 4 # 상 우 6 하 좌
    return direction

def start():
    direction = 0   # 처음 방향(우)
    time = 0    # 시작한 뒤 시간
    x,y = 1,1
    arr[x][y] = 2   # 뱀의 위치
    index = 0   # 다음 방향
    q = [(x,y)] # 뱀이 차지하고 있는 위치 정보(꼬리가 앞쪽)

    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]

        # 맵 범위 내에 있고, 뱀의 몸통이 없는 위치라면
        if 1<= nx <= N and 1<=ny <=N and arr[nx][ny] != 2:

            # 사과가 없다면 이동 후에 꼬리 제거
            if arr[nx][ny] == 0:
                arr[nx][ny] = 2
                q.append((nx,ny))   # 이동
                px,py = q.pop(0)    # 꼬리 제거
                arr[px][py] = 0

            # 사과가 있다면 이동 후에 꼬리 그대로 두기
            if arr[nx][ny] == 1:
                arr[nx][ny] = 2
                q.append((nx,ny))

        # 벽이나 뱀의 몸통과 부딪혔다면
        else:
            time += 1
            break

        # 다음 위치로 머리 이동
        x, y = nx, ny
        time += 1

        # 회전할 시간이면 회전
        if index < L and time == turn[index][0]:
            direction = bam_turn(direction, turn[index][1])
            index += 1

    return time



print(start())