# 3자리수 v 를 찾으면 탐색 중단

def f(i, N, K, v):
    if i==N:
        s = A[0]*100+A[1]*10+A[2]
        print(s)
        if s==v:
            return 1
        else:
            return 0
    else:
        for j in range(1, K+1):
            A[i] = j
            if f(i+1, N, K, v):
                return 1
        return 0

N = 3
K = 5
A = [0]*N
v = 125
print(f(0, N, K, v))