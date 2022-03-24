def find_set(antena):
    sum_distacne = 0
    for i in house:
        sum_distacne += abs(antena-i)
    return sum_distacne

N = int(input())
house = list(map(int,input().split()))
house.sort()

mmin = N * max(house)

for i in range(N):
    if mmin > find_set(house[i]):
        mmin = find_set(house[i])
        house_num = house[i]
