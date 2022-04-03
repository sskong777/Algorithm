import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1,T+1):
    day, month, month_3,year = map(int,input().split())
    arr = [0] + list(map(int,input().split()))

    # 월 별 누적된 값을 넣어줄 배열
    D = [0] * 13
    for i in range(1,13):
        mmin = D[i-1] + (arr[i]*day)
        mmin = min(mmin, D[i-1] + month)
        if i>=3:
            mmin = min(mmin,D[i-3] + month_3)
        if i>=12:
            mmin = min(mmin,D[i-12] + year)
        # i월까지의 누적 최소값!
        D[i] = mmin
    print(f'#{tc} {D[12]}')