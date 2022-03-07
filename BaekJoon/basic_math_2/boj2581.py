start = int(input())
end = int(input()) + 1

sieve = [True] * (end)
m = int(end ** 0.5)

for i in range(2,m+1):
    if sieve[i] == True:
        for j in range(i+i,end,i):
            sieve[j] = False
sieve[1] = False
# print(sieve)

prime = [i for i in range(start,end) if sieve[i] == True]
# print(prime)
if len(prime) == 0:
    print(-1)
else:
    print(sum(prime))
    print(min(prime))