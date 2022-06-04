import sys
sys.stdin = open('input.txt', 'r')

from itertools import combinations

N,M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]

# print(arr)
chick = []
house = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            house.append((i,j))
        if arr[i][j] == 2:
            chick.append((i,j))

comb = list(combinations(chick,M))
# print(comb)

result = 999999
# 치킨거리의 최솟값 구하기
for com in comb:
    temp = 0
    for hi,hj in house:
        distance = 10000
        for si,sj in com:
            distance = min(distance,abs(hi-si)+ abs(hj-sj))
        temp += distance
    result = min(result,temp)

print(result)