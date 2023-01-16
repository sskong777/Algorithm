import sys
sys.stdin = open('input.txt', 'r')

def turn():
    global direc
    direc -= 1
    if direc == -1:
        direc = 3


di = [-1,0,1,0]
dj = [0,1,0,-1]

N, M = map(int,input().split())
si,sj, direc = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]

visited = [[0]* M for _ in range(N)]
i,j = si,sj
cnt = 1
turn_time = 0
while True:
    turn()
    ni,nj = i+di[direc],j+dj[direc]
    if visited[ni][nj] == 0 and arr[ni][nj] == 0:
        visited[ni][nj] = 1
        turn()
        i,j = ni,nj
        cnt += 1
        turn_time = 0
    else:
        turn_time += 1

    if turn_time == 4:
        ni, nj = i - di[direc], j - dj[direc]
        if arr[ni][nj] == 0:
            i,j = ni,nj
        else:
            break
        turn_time = 0
print(cnt)