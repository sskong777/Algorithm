import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]  # N x N 행렬 만들어 두기

    # 우하좌상
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    r = 0
    c = 0
    num = 1
    arr[r][c] = num  # 시작은 1로 고정

    # 배열 크기만큼 반복
    while num < N * N:
        for direct in range(4):
            # 이동하려는 값을 살펴보기 위해 계산
            next_row = r + dr[direct]
            next_col = c + dc[direct]

            # 범위 내이고 현재 값이 0일 때만 반복
            while (0 <= next_row < N and 0 <= next_col < N) and arr[next_row][next_col] == 0:  # 0이 없으면 뚫고 지나가버림
                # 다음 인덱스가 사용가능하면 값 변경
                r = next_row
                c = next_col
                num += 1
                arr[r][c] = num

                # 다음 값이 범위 밖인지 확인하기 위해 계산
                next_row = r + dr[direct]
                next_col = c + dc[direct]

    print(f'#{tc}')
    for row in arr:
        print(*row)


