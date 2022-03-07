M, N = map(int, input().split())
N += 1
sieve = [True] * N
m = int(N ** 0.5)
for i in range(2,m+1):
    if sieve[i] == True:
        for j in range(i+i,N,i):
            sieve[j] = False
sieve[1] = False
prime = [i for i in range(M,N) if sieve[i] == True]
for i in prime:
    print(i)