import sys
R, C = map(int, sys.stdin.readline().split())
arr = [list(map(str, sys.stdin.readline().strip())) for _ in range(R)]

visited = [[0] * C for _ in range(R)]
visited[0][0] = 1
alphabets = set()
alphabets.add(arr[0][0])
answer = 0


def dfs(ci, cj, alphabets, cnt):
    global answer
    answer = max(answer, cnt)
    for di, dj in (-1, 0), (0, -1), (1, 0), (0, 1):
        ni, nj = ci + di, cj + dj
        if 0 <= ni < R and 0 <= nj < C and not visited[ni][nj] and arr[ni][nj] not in alphabets:
            alphabets.add(arr[ni][nj])
            visited[ni][nj] = 1
            dfs(ni, nj, alphabets, cnt + 1)
            visited[ni][nj] = 0
            alphabets.remove(arr[ni][nj])


dfs(0, 0, alphabets, 1)
print(answer)
