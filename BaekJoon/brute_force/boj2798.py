# 시간초과

N, M = map(int,input().split())
cards = list(map(int,input().split()))

# print(cards)

sub_set_arr =[]
# subset으로 풀이
for i in range(1 << N):
    sub_set = []
    for j in range(N):
        if i & (1<<j):
            sub_set.append(cards[j])
    if len(sub_set) == 3:
        sub_set_arr.append(sub_set)

flag = True
while flag:
    for i in sub_set_arr:
        if sum(i) == M:
            print(M)
            flag = False
            break
    M -= 1