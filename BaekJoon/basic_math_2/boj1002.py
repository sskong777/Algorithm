# 1. 두 좌표의 거리를 계산
# 2. 두 좌표를 중심으로 원이 겹치면 2
#    한 점으로 만나면 1
#    겹치지 않으면 0

T = int(input())
for tc in range(1,T+1):

    x1, y1, r1, x2, y2, r2 = map(int,input().split())

    x = abs(x1-x2)
    y = abs(y1-y2)
    # r1,r2 거리
    r_e = r1+r2
    r_i = abs(r1-r2)

    # 좌표 사이 거리 구하기
    distance = (x**2 + y**2) ** 0.5

    if x1 == x2 and y1 == y2:
        if r1 ==r2:
            print(-1)
        else:
            print(0)

    # 외접과 내접 고려
    else:
        if distance == r_i or distance == r_e:
            print(1)
        elif distance < r_e and distance > r_i:
            print(2)
        else:
            print(0)