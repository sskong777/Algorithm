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

sieve = [True] * 1000
sieve[0] = False
m = int(1000 ** 0.5)
for i in range(2,m+1):
    if sieve[i] == True:
        for j in range(i+i,1000,i):
            sieve[j] = False
prime_list = [i for i in range(2,1000) if sieve[i] == True]
# print(prime_list)

n = int(input())
arr = list(map(int,input().split()))

count = 0
for num in arr:
    if num in prime_list:
        count += 1
print(count)