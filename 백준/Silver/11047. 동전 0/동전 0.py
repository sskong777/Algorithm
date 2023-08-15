N,M = map(int,input().split())
arr = []

for i in range(N):
    arr.append(int(input()))

sum = 0
count = 0
money = M
# while sum == M:
for coin in arr[::-1]:
    # print(coin)
    count += money // coin
    money = money % coin
    # sum = count * coin + money
print(count)