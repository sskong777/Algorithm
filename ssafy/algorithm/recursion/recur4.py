# 1,2,3을 사용해 3자리수 만들기
def f(i, N):
    if i==N:
        print(A)
    else:
        for j in range(1, 4):
            A[i] = j
            f(i+1, N)
    return

N = 3
A = [0]*N
f(0, N)