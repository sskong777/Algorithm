import sys
sys.stdin = open('input.txt', 'r')

def bfs(S):
    q = []
    q.append(S)
    visited[S] = 1

    while q:
        now = q.pop(0)
        if now == G:
            return visited[now]-1
        for i in now+U, now-D:
            if 0<i<=F and not visited[i]:
                q.append(i)
                visited[i] = visited[now]+1
    return "use the stairs"




F, S, G, U, D = map(int,input().split())
visited = [0] * (F+1)
ans = bfs(S)
print(ans)