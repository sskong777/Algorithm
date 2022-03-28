# 부분집합 이용
def f(i, N, K):    # i 부분집합에 포함될지 결정할 원소의 인덱스, N 전체 원소개수, K 찾는 합

    if i==N:    # 한개의 부분집합 완성
        s = 0
        for j in range(N):
            if bit[j]:
                s += arr[j]
                # print(arr[j], end = ' ')
        # print(s)
        if s==K:    # 찾는 합이면
            for j in range(N):
                if bit[j]:
                    print(arr[j], end=' ')
            print()
    else:
        bit[i] = 1
        f(i+1, N, K)
        bit[i] = 0
        f(i+1, N, K)
    return

arr = [-1,3,-9,6,7,-6,1,5,4,2]
N = len(arr)
bit = [0] * N
f(0, N, 0)
