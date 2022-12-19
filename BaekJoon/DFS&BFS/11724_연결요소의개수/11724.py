import sys
sys.stdin = open('input.txt', 'r')

# 방향 없는 그래프가 주어졌을 때, 연결 요소 (Connected Component)의 개수를 구하는 프로그램을 작성하시오.
# 
# 입력
# 첫째 줄에 정점의 개수 N과 간선의 개수 M이 주어진다. (1 ≤ N ≤ 1,000, 0 ≤ M ≤ N×(N-1)/2) 둘째 줄부터 M개의 줄에 간선의 양 끝점 u와 v가 주어진다. 
# (1 ≤ u, v ≤ N, u ≠ v) 같은 간선은 한 번만 주어진다.

def bfs(v):
    q = []
    q.append(v)
    visited[v] = 1

    while q:
        now = q.pop(0)

        for i in graph[now]:
            if not visited[i]:
                q.append(i)
                visited[i] = 1


N, M = map(int,input().split())

graph = [[] for _ in range(N+1)]
visited = [0] * (N+1)
for i in range(M):
    u, v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

cnt = 0
for i in range(1, N+1):
    if not visited[i]:
        bfs(i)
        cnt +=1

print(cnt)