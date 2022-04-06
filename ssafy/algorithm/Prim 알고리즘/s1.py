'''
5 6
1 2 3
1 3 7
2 3 1
3 4 4
2 5 2
5 4 2
'''
def prim(start, V): # MST 가중치의 합을 리턴하는 함수. 1~V번 노드인 경우
    key = [INF] * (V + 1)  # key[i] i가 MST에 연결되는 비용
    key[1] = 0
    MST = [0] * (V + 1)
    pi = [0] * (V + 1)
    for _ in range(V):  # 모든 정점이 MST에 포함될 때 까지
        # MST에 포함되지 않은 정점 중 key[u]가 최소인 u 찾기
        u = 0
        minV = INF
        for i in range(1, V + 1):
            if MST[i] == 0:
                if key[i] < minV:
                    u = i
                    minV = key[i]
        MST[u] = 1  # key[u]가 최소인 u를 MST에 추가
        for v in range(V + 1):  # u에 인접인 v에 대해
            if MST[v] == 0 and adj[u][v] != 0:
                if key[v] > adj[u][v]:  # u를 이용해 기존보다 더 작은 비용으로 MST에 연결된다면
                    key[v] = adj[u][v]
                    pi[v] = u  # v는 u와 연결해서 MST에 포힘될 예정
    return sum(key[start:])  # MST 가중치의 합 리턴

V, E = map(int, input().split())
INF = 10000
# 인접행렬
adj = [[0]*(V+1) for _ in range(V+1)]

for _ in range(E):
    u, v, w = map(int, input().split())
    adj[u][v] = w
    adj[v][u] = w  #  무방향 그래프에서 MST 구성

#print(prim(0, V))  # 노드 시작 번호 0인 경우(교재 예시)
print(prim(1, V))  # 노드 시작 번호 1인 경우(코드 주석의 예시)



# 우선순위큐를 사용하지 않는 코드입니다.
'''
5 6
1 2 3
1 3 7
2 3 1
3 4 4
2 5 2
5 4 2
'''

V, E = map(int, input().split())
INF = 10000
# 인접행렬
adj = [[INF]*(V+1) for _ in range(V+1)]
for i in range(V+1):
    adj[i][i] = 0
for _ in range(E):
    u, v, w = map(int, input().split())
    adj[u][v] = w
    adj[v][u] = w  #  무방향 그래프에서 MST 구성
key = [INF]*(V+1)  # key[i] i가 MST에 연결되는 비용
key[1] = 0
MST = [0] * (V+1)
pi = [0] * (V+1)
for _ in range(V):  # 모든 정점이 MST에 포함될 때 까지
    # MST에 포함되지 않은 정점 중 key[u]가 최소인 u 찾기
    u = 0
    minV = INF
    for i in range(1, V+1):
        if MST[i]==0:
            if key[i] < minV:
                u = i
                minV = key[i]
    MST[u] = 1  # key[u]가 최소인 u를 MST에 추가
    for v in range(1, V+1):  # u에 인접인 v에 대해
        if MST[v] == 0 and u!=v and adj[u][v]< INF:
            if key[v] > adj[u][v]:  # u를 이용해 기존보다 더 작은 비용으로 MST에 연결된다면
                key[v] = adj[u][v]
                pi[v] = u    # v는 u와 연결해서 MST에 포힘될 예정
print(key)
print(pi)