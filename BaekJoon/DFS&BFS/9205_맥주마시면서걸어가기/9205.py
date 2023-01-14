import sys
sys.stdin = open('input.txt' , 'r')

def bfs():
    q = []
    q.append((sx,sy))

    while q:
        x,y = q.pop(0)
        if abs(x-rx) + abs(y-ry) <= 1000:
            print("happy")
            return
        for i in range(n):      # 편의점 체크
            if not visited[i]:  #편의점을 방문하지 않았다면
                pun_x,pun_y = pun[i]
                if abs(x-pun_x) + abs(y-pun_y)<=1000:   # 다음 거리까지 갈 수 있다면
                    visited[i] = 1
                    q.append((pun_x,pun_y))
    print("sad")
    return


T = int(input())

for tc in range(T):
    n = int(input())
    sx, sy = map(int,input().split())
    pun = []
    for i in range(n):
        x,y = map(int,input().split())
        pun.append((x,y))
    rx,ry = map(int,input().split())

    visited = [0 for _ in range(n+1)]
    bfs()