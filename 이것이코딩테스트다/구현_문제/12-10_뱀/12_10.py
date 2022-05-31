import sys
sys.stdin = open('input.txt', 'r')


def bam_turn(x,c):
    if c == 'L':
        x =



def start():




dx = [-1,0,1,0]
dy = [0,1,0,-1]

N = int(input())
K = int(input())
arr = [[0] * N for i in range(N)]


for k in range(K):
    r,c = map(int,input().split())
    arr[r-1][c-1] = 1


L = int(input())
turn = {}
for l in range(L):
    x,c = input().split()
    turn[int(x)] = c
# print(turn)
