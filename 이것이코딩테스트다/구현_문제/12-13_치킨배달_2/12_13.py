import sys
sys.stdin = open('input.txt', 'r')
from itertools import combinations

N, M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
chickens = []
houses = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 2:
            chickens.append((i,j))
        if arr[i][j] == 1:
            houses.append((i,j))
combi_chicken = combinations(chickens,M)

answer = 1e9
for combi in combi_chicken:
    dist = 0
    for hi,hj in houses:
        distance = 1e9
        for si,sj in combi:
            # "치킨거리" = 집과 가까운 치킨집 사이의 거리
            distance = min(distance,abs(hi-si)+ abs(hj-sj))

        dist += distance
    answer = min(dist,answer)
print(answer)