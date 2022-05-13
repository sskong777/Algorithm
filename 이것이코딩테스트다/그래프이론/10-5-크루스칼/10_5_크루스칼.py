import sys
sys.stdin = open('input.txt', 'r')

def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

V,E = map(int,input().split())

parent = [0] * (V+1)

# 모든 간선을 담을 리스트와 최종 비용을 담을 변수
edges = []
result = 0

# 부모테이블 상에서, 부모를 자기 자신으로 초기화
for i in range(1,V+1):
    parent[i] = i

# 모든 간선에 대한 정보를 입력받기
for _ in range(E):
    a,b,cost = map(int,input().split())
    edges.append((cost,a,b))

# 간선을 비용순으로 정렬
edges.sort()

# 간선을 하나씩 확인하며
for edge in edges:
    cost, a, b = edge
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
        result += cost
print(result)