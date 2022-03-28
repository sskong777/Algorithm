# 선택 정렬 함수(Selection Sort)를 재귀적 알고리즘으로 작성해 보시오.
A = [6,3,12,56,43,88,32,36,865,12,1,2,5,7,34]
N = len(A)

def selection_sort(idx):
    # global A//
    if idx == N:
        return
    mmin = idx
    for i in range(idx+1,N):
        if A[mmin] > A[i]:
            A[mmin],A[i] = A[i],A[mmin]
    return selection_sort(idx+1)

selection_sort(0)
print(A)