import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    # N개의 버스노선이 다니는 정류장 번호의 배열을 담아줄 배열.
    bus_array = []
    for i in range(N):
        bus = [] # i번째 노선이 다니는 정류장 번호
        a, b = map(int,input().split())
        bus = [i for i in range(a,b+1)]
        bus_array.append(bus)

    P = int(input())
    c_arr = []
    # P개 만큼 c(버스정류장)입력받고 c_arr에 추가
    for p in range(P):
        c = int(input())
        c_arr.append(c)

    # c(버스정류장)을 지나는 노선의 갯수를 담아줄 cnt_arr배열 생성
    cnt_arr = []

    # 3중 for문,,
    # for c in range(len(c_arr)):
    #     # c(버스정류장)이 바뀔때마다 cnt초기화
    #     cnt = 0
    #     for i in bus_array:
    #         for j in range(len(i)):
    #             if i[j] == c_arr[c]:
    #                 cnt += 1
    #     cnt_arr.append(cnt)

    # in연산자로 2중 for문
    for c in range(len(c_arr)):
        # c(버스정류장)이 바뀔때마다 cnt초기화
        cnt = 0
        for i in bus_array:
            if c_arr[c] in i:
                cnt += 1
        cnt_arr.append(cnt)

    print("#{}".format(tc), *cnt_arr)