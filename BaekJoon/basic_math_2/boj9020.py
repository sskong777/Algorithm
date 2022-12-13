def prime(N):
    sieve = [True] * N
    m = int(N ** 0.5)

    for i in range(2,m+1):
        if sieve[i] == True:
            for j in range(i+i,N,i):
                sieve[j] = False
    return [i for i in range(2,N) if sieve[i] == True]

T = int(input())
for tc in range(1,T+1):

    N = int(input())
    prime_list = prime(N)
    print(prime_list)
    partition = []
    for i in prime_list:
        for j in prime_list:
            if i < j:
                break
            if i + j == N :
                partition.append([i,j])
    # print(partition)
    min = 10000
    for i in partition:
        # print(i[0]-i[1])
        if (i[0] - i[1]) < min:
            min = (i[0] - i[1])
            res = i
    print(res[1], res[0])