import sys
sys.stdin = open('input.txt', 'r')

def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_find(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

N,M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]

parent = [0] * (N+1)
for i in range(1,N+1):
    parent[i] = i

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            union_find(parent,i+1,j+1)

plan = list(map(int,input().split()))
result = True
for i in range(M-1):
    if find_parent(parent,plan[i]) != find_parent(parent,plan[i+1]):
        result = False

if result:
    print('Yes')
else:
    print('No')
