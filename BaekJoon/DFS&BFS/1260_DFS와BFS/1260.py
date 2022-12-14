import sys
sys.stdin = open('input.txt', 'r')

# 그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고,
# 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.
#
# 입력
# 첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다.
# 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.

from collections import deque
def dfs(V):
    print(V, end=' ')
    visited[V] = 1                                      # 방문 후, 방문 처리
    for i in graph[V]:                                  # V와 연결된 정점을 순회
        if not visited[i]:                              # 방문하지 않았다면
            dfs(i)                                      # dfs 호출(재귀)



def bfs(V):
    q = []
    q.append(V)                                         # queue에 방문 노드 삽입
    visited[V] = 1                                      # 방문 처리

    while q:
        next = q.pop(0)                                 # queue를 순회
        print(next, end= ' ')
        for i in graph[next]:                           # 꺼낸 요소와 연결된 노드들을 순회
            if not visited[i]:                          # 방문하지 않았다면
                q.append(i)                             # queue에 삽입
                visited[i] = 1                          # 방문 처리

# deque bfs 사용

# def bfs(v):
#     q = deque([v])
#     visited[v] = 1
#
#     while q:
#         next = q.popleft()
#         print(next,end=' ')
#         for i in graph[next]:
#             if not visited[i]:
#                 q.append(i)
#                 visited[i] = 1

N, M, V = map(int,input().split())                      # 정점, 간선, 시작하는 정점번호


graph = [[] for _ in range(N+1)]                        # 인덱싱을 편하게 하기 위해 0을 포함하여 graph 생성
for m in range(M):                                      # 간선의 개수만큼 반복
    start, end = map(int,input().split())               # 시작점과 끝점을 입력받아서 graph에 추가(양방향)
    graph[start].append(end)
    graph[end].append(start)
# print(graph)
for i in range(N+1):
    graph[i].sort()
visited = [0] * (N+1)
dfs(V)

print()

visited = [0] * (N+1)
bfs(V)


