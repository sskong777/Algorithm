import sys
sys.stdin = open('input.txt', 'r')
# direction(북0, 동1, 남2, 서3)

def turn():
    global direc
    direc -= 1
    if direc == -1:
        direc = 3

di = [-1,0,1,0]
dj = [0,1,0,-1]

N,M = map(int,input().split())
v = [[0]*M for _ in range(N)]
i,j,direc = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]


cnt = 0
turn_time = 0
while True:
    turn()
    ni,nj = i+di[direc], j+dj[direc]
    if 0<ni<=N and 0<=nj<M and arr[ni][nj]==0 and v[ni][nj] == 0:
        v[ni][nj] = 1
        i,j = ni,nj
        cnt += 1
        turn_time = 0
    else:
        turn_time += 1
    if turn_time == 4:
        ni = i - di[direc]
        nj = j - dj[direc]
        if arr[ni][nj] == 0:
            i = ni
            j = nj
        else:
            break
        turn_time = 0
print(cnt)
