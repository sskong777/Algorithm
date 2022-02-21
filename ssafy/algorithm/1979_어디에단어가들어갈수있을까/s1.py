import sys
sys.stdin = open('input.txt', 'r')

def find_word(arr, N):
    sol = 0
    for r in range(N):
        cnt = 0
        for c in range(N):
            if arr[r][c] == 1:
                cnt += 1
            else:
                if cnt == K:
                    sol += 1
                cnt = 0
        if cnt ==K:
            sol += 1
    return  sol
T = int(input())
for tc in range(1,T+1):
    # 입력받아 arr, arr_T 생성
    arr = []
    N, K = map(int, input().split())
    for n in range(N):
        arr.append(list(map(int, input().split())))
    arr_T = list(zip(*arr))

    # sol = 0
    # for r in range(N):
    #     cnt = 0
    #     for c in range(N):
    #         if arr[r][c] == 1:
    #             cnt += 1
    #         else:
    #             if cnt == K:
    #                 sol += 1
    #             cnt = 0
    #     if cnt ==K:
    #         sol += 1
    sol = find_word(arr,N)
    sol += find_word(arr_T,N)
    print("#{} {}".format(tc, sol))