import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(T):
    K = int(input())
    arr = [list(map(int,input().split())) for _ in range(4)]

    for k in range(K):
        num, rot = map(int,input().split())     #자석번호와 회전방향

        print(num,rot)
    print(arr)
