import heapq
import sys
sys.stdin = open('input.txt', 'r')

INF = int(1e9)

T = int(input())

dx = [-1,0,1,0]
dy = [0,1,0,-1]

for tc in range(T):
    N = int(input())

    graph = []
    for i in range(N):
        graph.append(list(map(int,input().split())))

    # 최단 거리 테이블을 모두 무한으로 초기화
    distance = [[INF] * N for _ in range(N)]
    # 시작 위치
    x,y = 0,0
    q = [(graph[x][y], x, y)]
    distance[x][y] = graph[x][y]

    while q:
        # 가장 최단 거리가 잛은 노드에 대한 정보를 꺼내기
        dist, x, y = heapq.heappop(q)
        if distance[x][y] < dist:
            continue

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny <0 or ny >= N:
                continue

            cost = dist + graph[nx][ny]
            if cost < distance[nx][ny]:
                distance[nx][ny] = cost
                heapq.heappush(q, (cost, nx,ny))

    print(distance[N-1][N-1])


