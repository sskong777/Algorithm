import sys

sys.stdin = open('input.txt', 'r')

for tc in range(1):
    nc, ec = map(int, input().split())  # Node count, Edge count
    e = list(map(int, input().split()))  # 모든 경로 받기

    # 방문 경로를 저장할 2차원 리스트
    # 방향이 없기에 양방향으로 이동 가능함을 1로 나타냄
    # G[출발점][도착점] = 1
    # G[도착점][출발점] = 1
    G = [[0] * (nc + 1) for _ in range(nc + 1)]
    # 연결경로는 8개
    for idx in range(ec):
        G[e[idx * 2]][e[idx * 2 + 1]] = 1
        G[e[idx * 2 + 1]][e[idx * 2]] = 1

    visited = [False] * (nc + 1)
    stack = []

    # 노드 이동, stack에 추가, visited 작성 (반복)
    now = e[0]           # 시작 노드
    stack.append(now)    # 시작 노드 stack 에 추가
    visited[now] = True  # 시작 노드 방문 처리
    print(now, end=' ')  # 시작 노드 출력
    while stack:
        # 다음 노드를 탐색 하는 루프
        for nxt in range(nc + 1):
            if G[now][nxt] == 1 and visited[nxt] == 0:  # now 에서 이동 가능하고 방문한적 없는 nxt 노드가 있는지 확인
                # 노드 이동, stack에 추가, visited 작성
                now = nxt            # 다음 노드로 이동
                stack.append(now)    # 이동한 노드 stack 에 추가
                visited[now] = True  # 이동한 노드 방문 처리
                print(now, end=' ')  # 이동한 노드 출력
                break                # 이동한 노드에서 다음 노드를 탐색하기 위해 루프 종료
        else:  # 더 이상 방문할 노드가 없는 경우
            now = stack.pop()  # 이전 노드로 돌아간다


