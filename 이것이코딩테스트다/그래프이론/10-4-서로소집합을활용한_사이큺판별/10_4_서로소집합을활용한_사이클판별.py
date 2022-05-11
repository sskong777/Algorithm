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

# 부모테이블 상에서, 부모를 자기 자신으로 초기화
for i in range(1,V+1):
    parent[i] = i
# print(parent)
cycle = False

for i in range(E):
    a,b = map(int,input().split())
    # 사이클이 발생한 경우 종료
    if find_parent(parent,a) == find_parent(parent,b):
        cycle = True
        break
    else:
        union_parent(parent,a,b)

if cycle:
    print('사이클이 발생하였습니다.')
else:
    print('사이클이 발생하지 않았습니다')