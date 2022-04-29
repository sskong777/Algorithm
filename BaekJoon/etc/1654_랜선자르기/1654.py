import sys
sys.stdin = open('input.txt', 'r')

def binary_search(array,target,start,end):
    while start <= end:
        mid = (start+end)//2

        if array[mid] == target:
            return mid

        #중간점의 값보다 찾고자하는 값이 작은경우, - 왼쪽 확인
        elif array[mid] > target:
            end = mid - 1
        # 중간점의 값보다 찾고자 하는 값이 더 큰 경우 - 오른쪽 확인
        else:
            start = mid + 1
    return



K,N = map(int,input().split())
arr = [int(input()) for _ in range(K)]
start = 1
end = max(arr)

