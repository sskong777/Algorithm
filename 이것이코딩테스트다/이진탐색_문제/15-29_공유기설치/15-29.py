import sys
sys.stdin = open('input.txt', 'r')

# 1. array라는 리스트에 집들의 좌표를 입력받은 후에 정렬.
# 2. start = 1, end = array[-1] - array[0] 으로 설정. ( 시작값은 최소 거리, 끝 값은 최대 거리 )
# 3. 앞 집부터 공유기 설치
# 4. 설치할 수 있는 공유기 개수가 c개를 넘어가면 더 넓게 설치할 수 있다는 이야기 이므로 설치거리를 mid + 1로 설정하여 다시 앞집부터 설치.
# 5. c개를 넘어가지 않는다면 더 좁게 설치해야 한다는 이야기 이므로 mid - 1로 설정.

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