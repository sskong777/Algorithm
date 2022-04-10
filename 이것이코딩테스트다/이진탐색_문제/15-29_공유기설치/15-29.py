import sys
sys.stdin = open('input.txt', 'r')

def binary_search(arr,start,end):
    while start <= end:
        mid = (start+end)//2
        # 첫번째 집에 공유기 설치, 공유기 갯수 카운트
        current = arr[0]
        cnt = 1

        for i in range(1,len(arr)):
            if arr[i] >= current+mid:
                cnt += 1
                current = arr[i]

        if cnt >= C:
            start = mid + 1
            res = mid
        else:
            end = mid-1
    return res



N,C = map(int,input().split())
arr = [int(input()) for _ in range(N)]
arr.sort()

start, end = 1,(arr[-1] - arr[0])

res = binary_search(arr,start,end)
print(res)