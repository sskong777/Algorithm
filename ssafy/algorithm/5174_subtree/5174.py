import sys
sys.stdin = open('input.txt', 'r')
#
# def is_c(N):
#     global res
#     if c1[N]:
#         res += 1
#         N = c1[N]
#         is_c(N)
#     if c2[N]:
#         res += 1
#         N = c2[N]
#         is_c(N)

def pre_order(N):
    global res
    if N:
        res += 1
        pre_order(c1[N])
        pre_order(c2[N])

T = int(input())
for tc in range(1,T+1):
    E, N = map(int,input().split())
    arr = list(map(int,input().split()))

    V = E + 1
    c1 = [0] * (V+1)
    c2 = [0] * (V+1)
    # par= [0] * (V+1)

    for i in range(E):
        # 2 1 2 5 1 6 5 3 6 4
        p, c = arr[i*2], arr[i*2 + 1]
        if c1[p] == 0:
            c1[p] = c
        else:
            c2[p] = c
    # print(c1)   [0, 6, 1, 0, 0, 3, 4]
    # print(c2)   [0, 0, 5, 0, 0, 0, 0]

    res = 0
    pre_order(N)
    print(f'#{tc} {res}')
