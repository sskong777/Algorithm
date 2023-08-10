# https://www.acmicpc.net/problem/2178
# DFS/ BFS
import time
import sys
# input = sys.stdin.readline
# N = 100
# M = 100
# time :1s => 40,000,000
# 시간 복잡도 : O(?)
from collections import deque

def bfs(si,sj):
    q = deque()
    q.append((si,sj))
    visited[si][sj] = 1

    while q:
        ci,cj = q.popleft()
        for di,dj in (-1,0),(1,0),(0,1),(0,-1):
            ni,nj = ci+di, cj+dj
            if 0<=ni<n and 0<=nj<m and arr[ni][nj] == 1 and not visited[ni][nj]:
                q.append((ni,nj))
                visited[ni][nj] = visited[ci][cj] + 1
    return visited[n-1][m-1]

n, m = map(int,input().split())
arr = [list(map(int,list(input()))) for _ in range(n)]
visited = [[0]*(m) for _ in range(n)]

res = bfs(0,0)
print(res)