import sys
sys.stdin = open('input.txt', 'r')

def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

V,E = map(int,input().split())
parent = [0] * (V+1)

edges = []
result = 0

for i in range(1,V+1):
    parent[i] = i

for i in range(E):
    a, b, cost = map(int,input().split())
    edges.append((cost,a,b))

edges.sort()
last = 0
for edge in edges:
    cost,a,b = edge
    # 사이클이 생기지 않는다면
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
        # 거리를 더해준다.
        result += cost
        last = cost # 마지막 값 구하기

print(result-last)