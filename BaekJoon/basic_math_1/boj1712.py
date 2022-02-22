a, b, c = map(int,input().split())

if c <= b:
    print(-1)
else:
    # A + (B * N) < (C * N) 이어야 이득이다.
    # --> A + (B-C)*N 으로 나눈 값의 몫 + 1일 때부터 이득이 생긴다.
    print(int(a/(c-b))+1)