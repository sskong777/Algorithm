import sys
sys.stdin = open('input.txt', 'r')


def in_order(v):
    global N
    if v <= N:
        in_order(v*2)
        arr.append(v)
        in_order(v*2 + 1)

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    tree = [0] * (N+1)
    arr = [0]
    in_order(1)

    # print(arr)    [0, 4, 2, 5, 1, 6, 3]
    for i in range(1,N+1):
        tree[arr[i]] = i
    # print(tree)   [0, 4, 2, 6, 1, 3, 5]

    print(f'#{tc} {tree[1]} {tree[N//2]}')


