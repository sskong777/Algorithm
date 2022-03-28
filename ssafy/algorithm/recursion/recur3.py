# def f(i, N): #  A[i]에 0 또는 1을 채우는 함수
#     if i==N:    # A가 채워진 경우
#         print(A)
#     else:
#         A[i] = 0
#         f(i+1, N)
#         A[i] = 1
#         f(i+1, N)
#     return
def f(i, N): #  A[i]에 0 또는 1을 채우는 함수
    if i==N:    # A가 채워진 경우
        print(A)
    else:
        for j in range(2):
            A[i] = j
            f(i+1, N)
    return

N = 3
A = [0]*N
f(0, N)