N = int(input())
house = list(map(int,input().split()))

# 오름 차순으로 정렬
house.sort()

# 집의 위치들 중 가운데에 있는 집에 위치에 안테나를 설치하는 것이 최소 거리가 나옴

house_num = 0

# N(집의 갯수)이 짝수일때와 홀수 일 때를 나눠서 안테나를 설치할 위치를 정해야한다)
if N % 2 == 1:
    house_num = N//2
else:
    house_num = N//2 -1

print(house[house_num])