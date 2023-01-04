import sys
sys.stdin = open('input.txt', 'r')

def bfs(A):
    q = []
    q.append((A,1))

    while q:
        num, time = q.pop(0)

        if num == B:
            print(time)
            return
        if num * 2 <= B:
            q.append(((num * 2), time + 1))
        if (num*10 + 1) <= B:
            q.append((num*10 + 1, time +1))

    print(-1)

A, B = map(int,input().split())
bfs(A)
