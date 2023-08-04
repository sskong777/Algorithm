from collections import deque

def bfs(start):
    q = deque()
    q.append(start)
    # visited[start] = 1
    distance[start] = 0
    while q:
        now = q.popleft()

        if now == e:
            break
        for next in (now-1, now+1, now+5):
            if 0 < next <= 10000:
                if not distance[next]:
                    q.append(next)
                    # distance[next] = 1
                    distance[next] = distance[now] + 1



s,e = map(int,input().split())
distance = [0] * 10001
# visited = [0] * 10001

bfs(s)
print(distance[e])