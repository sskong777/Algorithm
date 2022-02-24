def f(i, N):
    if i==N:
        return
    else:
        B[i] = A[i]
        f(i+1, N)

A = [10, 20, 30]
B = [0]*3
f(0, 3)
print(B)