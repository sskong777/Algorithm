import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    # K는 1회 충전으로 갈 수 있는 정류장 수, N은 정류장 수, M은 충전기가 설치된 정류장 갯수
    stop = [0] * (N+1) # 버스 정류장의 수만큼 길이를 가지는 리스트를 생성한다.
    list_ = list(map(int, input().split())) # 충전기가 설치된 정류장의 번호를 지닌 리스트를 생성한다.
    for i in list_:
        stop[i] = 1 # 충전기가 설치된 지점(인덱스)마다 해당 인덱스 값을 1로 바꿔준다.

    idx = 0 # 버스의 현재 위치
    cnt = 0 # 충전 횟수

    while True:
        idx += K # 일단 버스가 충전되었다고 가정하고 버스를 움직일 수 있는 최대한 만큼 움직인다
        if idx >= N: # 버스가 종점에 도착하거나 혹은 지나가는 경우에는 while문을 빠져나온다.
            break

        for i in range(idx, idx-K, -1): # 버스가 충전되어서 최대한 움직일 수 있는 위치로 이동후 다시 역으로 충전기가 있는지 유무를 파악해본다.
            if stop[i] == 1: # 지나왔던 정류소에 충전기가 있었다면
                cnt += 1 # 충전횟수를 1씩 증가시킨다.
                idx = i # 충전을 통해 갈 수 있음이 확인되었으므로 해당 위치로 버스를 이동시킨다.
                break
        else: # 충전을 할 수 없는 경우
            cnt = 0 # 충전횟수에 0을 대입하고
            break #while문을 빠져나온다.

    print(f'#{tc} {cnt}')

