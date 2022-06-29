import sys
sys.stdin = open('input.txt', 'r')

def rotate():

    pass



T = int(input())
for tc in range(T):
    K = int(input())
    arr = [list(map(int,input().split())) for _ in range(4)]

    for k in range(K):
        num, rot = map(int,input().split())     #자석번호와 회전방향



