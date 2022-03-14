def prime_count(n):
    end = 2*n + 1
    sieve = [True] * end
    m = int(end ** 0.5)

    for i in range(2,m+1):
        if sieve[i] == True:
            for j in range(i+i,end,i):
                sieve[j] = False

    prime_list = [i for i in range(n+1,end) if sieve[i] == True]
    return len(prime_list)
#
# res = prime_count(100000)
# print(res)

while True:
    a = int(input())
    if a == 0:
        break
    res = prime_count(a)
    print(res)