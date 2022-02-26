import sys
sys.stdin = open('input.txt')

for _ in range(1, 11):
    tc = int(input())
    matrix = [list(map(int, input().split())) for _ in range(100)]

    # 출발점 -> 시작점
    for col_x in range(100):
        # 도착지는 값이 2
        if matrix[99][col_x] == 2:
            # 도착지의 좌표를 저장
            row, col = 99, col_x

    # delta 값
    # 좌 우 상 -> 도착지부터 올라가기 때문에 아래는 볼 필요 없음
    dr = [0, 0, -1]
    dc = [-1, 1, 0]

    # 가장 윗부분에 도달하면 끝내자
    while row != 0:
        # 주위를 둘러보고 왼쪽이나 오른쪽으로 갈 길이 있으면 가자
        # 방향 델타로 이동
        for i in range(3):
            # 좌->우->상
            # 좌표 변경
            next_r = row + dr[i]
            next_c = col + dc[i]

            # 새로운 위치로 옮겼을 때 그 위치가
            # matrix 범위 내에서 안에 포함되는지 확인하고
            if 0 <= next_r < 100 and 0 <= next_c < 100:
                # 현재 위치로부터 왼쪽/오른쪽/위쪽에 길이 있다면 (가야 할 곳으로 미리 탐색)
                if matrix[next_r][next_c]:
                    # 현재 위치는 0으로 만들고(그래야 다음 탐색에서 1을 보고 가지 않음)
                    matrix[row][col] = 0
                    # 현재 위치 갱신 -> 움직여야 할 곳으로 이동
                    row = next_r
                    col = next_c

    # 최종적으로 column값 출력
    print('#{} {}'.format(tc, col))