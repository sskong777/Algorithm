import sys
sys.stdin = open('input.txt', 'r')
# 부분집합의 합으로 구하기
N = int(input())
arr = list(map(int,input().split()))

lst = []
for i in range(1<<N):
    sub_set = []
    for j in range(N):
        if i & (1<<j):
            sub_set.append(arr[j])
    lst.append(sum(sub_set))

lst.sort()
print(lst)

res = 1
for i in range(1,max(lst)):
    if i not in lst:
        res = i
        break
print(res)