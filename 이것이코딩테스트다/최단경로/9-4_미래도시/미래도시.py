import sys
sys.stdin = open('input.txt', 'r')
INF = int(1e9)

# 노드의 개수, 간선의 개수
N,M = map(int,input().split())

# 2차원 리스트를 만들고, 모든 값을 무한으로 초기화
graph = [[INF]*(N+1) for _ in range(N+1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1,N+1):
    for b in range(1,N+1):
        if a==b:
            graph[a][b] = 0

# 각 간선에 대한 정보를 입력받아, 그 값으로 초기화
for _ in range(M):
    start,end = map(int,input().split())
    graph[start][end] = 1
    graph[end][start] = 1
# print(graph)

# 거쳐 갈 노드 K와 종점노드 X를 입력받기
K,X = map(int,input().split())

# 점화식에 따라 플로이드 워셜 알고리즘을 수행
# 점화식 : D[ab] = min(D[ab], D[ak]+D[kb])
for k in range(1,N+1):
    for a in range(1,N+1):
        for b in range(1,N+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

distance = graph[1][k] + graph[K][X]

if distance >= INF:
    print('-1')
else:
    print(distance)

