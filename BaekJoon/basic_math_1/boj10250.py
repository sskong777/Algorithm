T = int(input())
for tc in range(1,T+1):
    H, W ,N = map(int,input().split())
    if N % H:
        floor = (N % H) * 100
        ho = N // H + 1
    else:
        floor = H * 100
        ho = N // H
    print(floor + ho)

