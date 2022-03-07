# n까지 소수의 갯수 구하기
# 에라스토테네스의 체
def isPrime(n):
    sieve = [True] * n

    m = int(n ** 0.5)
    for i in range(2,m+1):
        if sieve[i] == True:    # i가 소수인 경우
            for j in range(i+i,n,i):    # i 이후의 배수들을 False로 변환
                sieve[j] = False

    return [i for i in range(2,n) if sieve[i] == True]  # sieve리스트에서 True(소수)인 i값만 리스트에 담아서 반환


n = int(input())
p = isPrime(n)
print(p)
