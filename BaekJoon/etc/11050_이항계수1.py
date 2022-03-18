# 이항계수 공식
# (N)
# (K)     --> n!/k!(n-k!)

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

N,K = map(int,input().split())
res = factorial(N) // (factorial(K) * factorial(N-K))
print(res)