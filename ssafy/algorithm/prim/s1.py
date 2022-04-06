import sys
sys.stdin = open('input.txt', 'r')


def prim(start):
    D[start] = 0

    for _ in range(V):
        # MST 에 포함되지 않은 정점 중에서 거리가 최소인 정점을 찾는
        min_v = 0
        min_d = INF
        for i in range(1, V+1):
            if MST[i] == 0:
                if D[i] < min_d:
                    min_d = D[i]
                    min_v = i

        MST[min_v] = 1   # MST에 등록
        for v in range(V+1):
            # 연결되지 않은 정점 중에서
            # 선택된 정점 min_v와 연결된 정점들을 찾아서 거리를 확인
            if adj[min_v][v] != 0 and MST[v] == 0:
                if D[v] > adj[min_v][v]:
                    D[v] = adj[min_v][v]
                    P[v] = min_v

    return sum(D[start:]), P


V, E = map(int, input().split())
INF = 987654321

adj = [[0] * (V+1) for _ in range(V+1)]
for _ in range(E):
    s, e, d = map(int, input().split())
    adj[s][e] = d
    adj[e][s] = d


MST = [0] * (V+1)    # MST 구성 여부
D = [INF] * (V+1)    # 최소 거리
P = [0] * (V+1)      # 연결된 부모

res = prim(1)
print(res)