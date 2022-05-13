import sys
sys.stdin = open('input.txt', 'r')

def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

N,M = map(int,input().split())
parent = [0] * (N+1)

# 부모 테이블 상에서 부모를 자기 자신으로 초기화
for i in range(N+1):
    parent[i] = i

for i in range(M):
    oper,a,b = map(int,input().split())
    if oper == 0:
        union(parent,a,b)
    elif oper == 1:
        # 사이클을 형성하지 않는다면
        if find_parent(parent,a) == find_parent(parent,b):
            print('YES')
        else:
            print('NO')
