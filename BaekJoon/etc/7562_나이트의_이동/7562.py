import sys
from collections import deque

sys.stdin = open('input.txt', 'r')

def bfs(si,sj):
    q = deque()
    q.append((si,sj))

T = int(input())
for tc in range(T):
    N = int(input())
    si,sj = map(int,input().split())
    ei,ej = map(int,input().split())

    v = [[0]*N for _ in range(N)]