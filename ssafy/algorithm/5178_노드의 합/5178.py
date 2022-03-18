import sys
sys.stdin = open('input.txt', 'r')


T = int(input())
for tc in range(1,T+1):
    V, M, L = map(int,input().split())
    # E = V - 1
    tree = [0] * (V+1)
    for m in range(M):
        c, n = map(int,input().split())      # 리프노드번호, 저장된 값
        tree[c] = n
    # print(tree) [0, 0, 0, 3, 1, 2]
    for i in range(V,0,-1):
        tree[i//2] += tree[i]
    print(tree)
    print(f'#{tc} {tree[L]}')