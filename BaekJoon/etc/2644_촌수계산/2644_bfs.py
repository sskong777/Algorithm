import sys
sys.stdin = open('input.txt', 'r')

def bfs(a):
    q = []
    q.append(a)
    # v[a] = 1

    while q:
        next = q.pop(0)
        for i in graph[next]:
            if not v[i]:
                v[i] = v[next] + 1
                q.append(i)


V = int(input())
a,b = map(int,input().split())
E = int(input())
graph = [[]*(V+1) for _ in range(V+1)]
v = [0] * (V + 1)

for e in range(E):
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

bfs(a)
if v[b] ==0 :
    print(-1)
else:
    print(v[b])