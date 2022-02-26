T = int(input())    # 테스트케이스 갯수 입력
for tc in range(1,T+1): # 테스트케이스 만큼 반복
    N, K = map(int, input().split())    # N차원 리스트의 가로 세로 길이 N 과 특정길이 K를 입력
    arr = []    # N차원 리스트를 구현할 arr배열 생성
    sum_arr = []    # 각 구간 합을 담아줄 sum_arr생성
    mmax = 0    # 구간 합의 배열인 sum_arr에서 최대값을 담아줄 변수. 요소들은 양의 정수이므로 0으로 초기화.
    # N번 만큼 반복하여 arr리스트에 N차원의 값들을 담아준다.
    for n in range(N):
        arr.append(list(map(int, input().split())))

    k_arr = []  # 각 행의 k만큼의 요소들을 담아줄 k_arr 생성
    for n in range(0,N):  # 각 행만큼 반복(N번만큼)
        # k_arr에 인덱스 슬라이싱으로 k개만큼의 요소들을 담아준다.(인덱스 슬라이싱은 범위를 초과해도 오류가 나지 않는다. )
        k_arr.append(arr[n][n:n+K])

    # k_arr 배열을 반복하여 k만큼의 구간합을 구해 sum_arr배열에 담아준다.
    for k in k_arr:
        total = 0   # total은 각 행을 돌 때 마다 초기화해준다,
        for num in k:
            total += num
        # 구간합은 sum_arr배열에 담아준다.
        sum_arr.append(total)

    # sum_arr에서 최대값을 구해준다.
    for s in sum_arr:   # sum_arr의 요소들을 반복하면서
        if s >= mmax:   # 각 구간합의 요소가 mmax보다 크면 mmax에 그 값을 넣어주어 최대값을 구한다.
            mmax = s
    print("#{} {}".format(tc, mmax))


