import sys
sys.stdin = open('input.txt')


def bfs(start):
    q = []
    q.append((start,1))
    visited[start] = 1

    while q:
        now, time = q.pop(0)

        if now == K:
            return visited[now]

        for i in now-1, now+1:
            if 0<=i<100001 and not visited[now]:
                q.append(i)
                visited[i] = 1





N, K = map(int,input().split())
visited = [0] * 100001

ans = bfs(N)
print(ans)
