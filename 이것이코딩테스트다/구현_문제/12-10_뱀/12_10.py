import sys
sys.stdin = open('input.txt', 'r')

from collections import deque

def bam_turn(x,c):
    if c == 'L':
        x = (x-1) % 4   # 상 좌 하 우
    else:
        x = (x+1) % 4 # 상 우 하 좌
    return x



def start():
    direction = 1
    time = 1
    y,x = 0,0
    visited = deque([[y,x]])
    arr[y][x] = 2
    while True:
        y,x = y+ dy[direction], x + dx[direction]
        if 0<= y < N and 0<= x < N and arr[y][x] != 2:
            if not arr[y][x] == 1:
                temp_y, temp_x = visited.popleft()
                arr[temp_y][temp_x] = 0     # 꼬리제거
            arr[y][x] = 2
            visited.append([y,x])
            if time in turn.keys():
                direction = bam_turn(direction, turn[time])
            time += 1
        else:
            return time


# 상 우 하 좌
dx = [-1,0,1,0]
dy = [0,1,0,-1]

N = int(input())
K = int(input())
arr = [[0] * N for i in range(N)]


for k in range(K):
    r,c = map(int,input().split())
    arr[r-1][c-1] = 1       # 과일 위치에 1 남기기


L = int(input())
turn = {}
for l in range(L):
    x,c = input().split()
    turn[int(x)] = c

print(start())