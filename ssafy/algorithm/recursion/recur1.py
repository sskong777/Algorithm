def f(i, N):
    if i==N:
        return
    else:
        B[i] = A[i]
        f(i+1, N)

N = 3
A = [10, 20, 30]
B = [0]*N
f(0, N)
print(B)