import sys
sys.stdin = open('input.txt', 'r')


def bfs(start):
    q = []
    q.append(start)
    global cnt
    while q:
        now = q.pop(0)
        if now == K:
            cnt += 1

        for i in now-1, now+1, now*2:
            if 0<=i<100001 and not visited[i]:
                q.append(i)
                visited[i] = visited[now] + 1



N, K = map(int,input().split())
visited = [0] * 100001
cnt = 0
bfs(N)
print(visited[K]-1)
print(cnt)
