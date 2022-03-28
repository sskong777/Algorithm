# 1~K (K>=3) 을 중복사용해 3자리수 만들기
def f(i, N, K):
    if i==N:
        print(A)
    else:
        for j in range(1, K+1):
            A[i] = j
            f(i+1, N, K)
    return

N = 3
K = 5
A = [0]*N
f(0, N, K)