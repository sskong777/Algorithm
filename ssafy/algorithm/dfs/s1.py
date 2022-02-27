import sys
sys.stdin = open('input.txt', 'r')

nc, ec = map(int, input().split())
edges = list(map(int, input().split()))

# 방문 경로를 저장할 2차원 리스트
G = [[0] * (nc+1) for _ in range(nc+1)]
# G[출발점][도착점] = 1
for idx in range(ec):
    # edges[idx * 2] 출발점, edges[idx*2 + 1] 도착점.
    G[edges[idx*2]][edges[idx*2+1]] = 1
    G[edges[idx*2 + 1]][edges[idx*2]] = 1
#<-------------준비단계------------------

visited = [False] * (nc+1)

start = edges[0]
stack = [start]

while stack:
    now = stack.pop()   # 현재 방문하고 있는 지점.

    if visited[now] == 0:    # 방문 했는지 검사
        visited[now] = True
        print(now, end= ' ')

        # 다음으로 갈 수 있는 노드를 탐색 -> G에 인접 노드 정보가 들어있다.
        # G[출발][도착] ==1 이면 이동 가능한 노드
        for nxt in range(nc, -1, -1):   # nc+1 해도됨
            if G[now][nxt] == 1 and visited[nxt] == 0:
                stack.append(nxt)
