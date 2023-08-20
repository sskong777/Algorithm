# def isPrime(n):
#     sieve = [True] * n
#
#     m = int(n ** 0.5)
#     for i in range(2,m+1):
#         if sieve[i] == True:    # i가 소수인 경우
#             for j in range(i+i,n,i):    # i 이후의 배수들을 False로 변환
#                 sieve[j] = False
#
#     return [i for i in range(2,n) if sieve[i] == True]  # sieve리스트에서 True(소수)인 i값만 리스트에 담아서 반환

def isPrime(N):
    sieve = [True] * (N+1)
    root = int(n**0.5)
    for i in range(2,root+1):
        if sieve[i] == True:
            for j in range(i+i,N+1,i):
                sieve[j] = False
    return [i for i in range(N+1) if sieve[i] == True]



def isPrime(n,m):
    sieve = [True] * (n+1)

    root = int(n ** 0.5)
    for i in range(2,root+1):
        if sieve[i] == True:    # i가 소수인 경우
            for j in range(i+i,n+1,i):    # i 이후의 배수들을 False로 변환
                sieve[j] = False

    return [i for i in range(m,n+1) if sieve[i] == True]  # sieve리스트에서 True(소수)인 i값만 리스트에 담아서 반환
m, n = map(int,input().split())

prime_list = isPrime(n,m)
for i in prime_list:
    print(i)