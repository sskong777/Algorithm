# A의 부분집합중 합이 K인 부분집합의 개수 구하기
def f(i, N, s, K):  # s i-1원소까지 고려된 부분집합의 합
    global cnt
    if i==N:
        if s==K:
            cnt += 1
    else:
        f(i+1, N, s+A[i], K) # A[i]포함
        f(i+1, N, s, K)

A = [1,2,3,4,5,6,7,8,9,10]
N = len(A)
K = 55
cnt = 0
f(0, N, 0, K)
print(cnt)