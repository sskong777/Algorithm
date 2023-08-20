# 4배 정도 빠름
def isPrime(m,n):
    sieve = [True] * (n+1)
    root = int(n ** 0.5)
    sieve[1] = False
    for i in range(2,root+1):
        if sieve[i] == True:    # 소수 라면
            for j in range(i+i,n+1,i):
                sieve[j] = False
    return [i for i in range(m,n+1) if sieve[i] == True]

num = int(input())
prime_list = isPrime(num,1005000)
# print(prime_list)
for prime in prime_list:
    if str(prime) == str(prime)[::-1]:
        print(prime)
        break


#
# import math
#
# def isPrime(x):
#     if x == 1:
#         return False
#     for i in range(2, int(math.sqrt(x)+1)):
#         if x % i == 0:
#             return False
#     return True
#
# def isPalindrome(x):
#     if str(x) == str(x)[::-1]:
#         return True
#     return False
#
# N = int(input())
# while True:
#     if isPrime(N) and isPalindrome(N):
#         print(N)
#         break
#     N += 1