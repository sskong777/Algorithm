import sys
from collections import deque

sys.stdin = open('input.txt', 'r')

def bfs(si,sj):
    q = deque()
    q.append((si,sj))
    v[si][sj] = 1

    while q:
        ci,cj = q.popleft()
        if ci==ei and cj==ej:
            return v[ci][cj]

        for di,dj in ((1,2),(-1,2),(-1,-2),(1,-2),(2,1),(2,-1),(-2,1),(-2,-1)):
            ni,nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<N and v[ni][nj]==0:
                q.append((ni,nj))
                v[ni][nj] = v[ci][cj] + 1
import sys
from collections import deque

sys.stdin = open('input.txt', 'r')

def bfs(si,sj):
    q = deque()
    q.append((si,sj))
    v[si][sj] = 1

    while q:
        ci,cj = q.popleft()
        if ci==ei and cj==ej:
            return v[ci][cj]

        for di,dj in ((1,2),(-1,2),(-1,-2),(1,-2),(2,1),(2,-1),(-2,1),(-2,-1)):
            ni,nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<N and v[ni][nj]==0:
                q.append((ni,nj))
                v[ni][nj] = v[ci][cj] + 1


T = int(input())
for tc in range(T):
    N = int(input())
    si,sj = map(int,input().split())
    ei,ej = map(int,input().split())

    v = [[0]*N for _ in range(N)]
    res = bfs(si,sj)
    print(res-1)

T = int(input())
for tc in range(T):
    N = int(input())
    si,sj = map(int,input().split())
    ei,ej = map(int,input().split())

    v = [[0]*N for _ in range(N)]
    res = bfs(si,sj)
    print(res-1)