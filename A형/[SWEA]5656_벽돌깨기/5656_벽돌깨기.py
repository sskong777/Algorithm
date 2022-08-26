import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(T):
    N, W, H = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(H)]
    # print(arr)


def bfs(si,sj):
    q = []
    visited = [[0]* N for _ in range(N)]
    visited[si][sj] = 1
