n = 1260
cnt = 0

coin = [500,100,50,10]
for co in coin:
    cnt += n // co
    n %= co
print(cnt)