import sys
sys.stdin = open('input.txt', 'r')

def in_order(v):
    if v <= V:
        in_order(v*2)
        print(tree[v],end='')
        in_order(v*2+1)

T = 10
for tc in range(1,T+1):
    V = int(input())
    tree = [0] *(V+1)
    for n in range(V):
        arr = list(input().split())
        tree[n+1] = arr[1]
    print(f'#{tc}',end=' ')
    in_order(1)
    print()