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

for i in range(E):
    a,b = map(int,input().split())
    union_parent(parent,a,b)

# print(parent)

# 각 원소가 속한 집합 출력
print('각 원소가 속한 집합 : ',end=' ')
for i in range(1,V+1):
    print(find_parent(parent,i),end=' ')

print()


# 부모 테이블 내용 출력
print('부모테이블 : ',end=' ')
for i in range(1,V+1):
    print(parent[i], end=' ')