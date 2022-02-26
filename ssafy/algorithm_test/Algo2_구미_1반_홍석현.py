T = int(input())    # 테스트케이스 갯수 입력
for tc in range(1, T+1):    # 테스트케이스 만큼 반복
    arr = []    # N차원 리스트를 담아줄 arr배열 선언
    N = int(input())
    for n in range(N):  # N만큼 반복하여 arr 배열에 입력받은 값을 담아준다.
        arr.append(list(map(int, input().split())))

    total_dir = []  # 4방향 합을 구해줄 배열 선언
    total_3x3 = []  # 3x3 배열의 합을 구해줄 배열 선언
    max_dir = 0     # 4방향 합의 최대값을 구해줄 변수 선언 및 초기화
    max_3x3 = 0     # 3x3 배열의 합의 최대값을 구해줄 변수 선언 및 초기화

    # dr = [0, 1, 0, -1]
    # dc = [1, 0, -1, 0]
    dr = [0, 1, 0, -1, 1, 1, -1, -1]
    dc = [1, 0, -1, 0, 1 ,-1, 1, -1]

    # 4방향 합
    for r in range(N):
        for c in range(N):
            total = arr[r][c]
            for i in range(1, arr[r][c]):
                for dir in range(4):
                    row = r + (dr[dir] * (i))
                    col = c + (dc[dir] * (i))
                    if 0 <= row <= N-1 and 0 <= col <= N-1:
                        total += arr[row][col]
            total_dir.append(total)
    max_dir = max(total_dir)


    # 3x3
    for r in range(N):
        for c in range(N):
            total2 = arr[r][c]
            for dir in range(8):
                row = r + (dr[dir])
                col = c + (dc[dir])
                if 0 <= row <= N - 1 and 0 <= col <= N - 1:
                    total2 += arr[row][col]
            total_3x3.append(total2)
    max_3x3 = max(total_3x3)

    print("#{}".format(tc), end=' ')
    print(max(max_dir, max_3x3))
