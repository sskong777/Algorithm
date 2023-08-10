# https://www.acmicpc.net/problem/2178
# DFS/ BFS
import time
import sys
# input = sys.stdin.readline
# N = 100,000
# time :1s => 40,000,000
# 시간 복잡도 : O(?)

# 5
# 1 3 2 -1
# 2 4 4 -1
# 3 1 2 4 3 -1
# 4 2 4 3 3 5 6 -1
# 5 4 6 -1
from collections import deque
def bfs(start):
    q = deque()
    q.append(start)
    visited[start] = 1

    while q:
        now = q.popleft()
        for next in graph[now]:
            if not visited[next[0]]:
                q.append(next[0])
                visited[next[0]] = 1
                distance[next[0]] = distance[now] + next[1]
    return distance
V = int(input())

graph = [[] for _ in range(V+1)]

for i in range(1,V+1):
    line = list(map(int,input().split()))
    v = line[0]
    for i in range(1,len(line)-1,2):
        graph[v].append((line[i],line[i+1]))
# print(graph)
visited = [0] * (V+1)
distance = [0] * (V+1)
# 아무 노드에서 bfs 시작
bfs(1)
# 아무 노드에서 가장 거리가 먼 노드 인덱스를 찾은 뒤 그 인덱스에서 bfs
result_index = distance.index( max(distance) )
visited = [0]*(V+1)
distance = [0] * (V+1)
bfs(result_index)
print(max(distance))