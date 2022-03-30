# 재귀를 이용한 binary_search
def binary_search(array,target,start,end):
    global cnt
    if start > end:
        return
    mid = (start+end)//2

    # 타켓을 찾았으면 타겟에 해당하는 인덱스를 제거한 후 다시 이진탐색을 돌린다.
    if array[mid] == target:
        cnt += 1
        array.pop(mid)
        return binary_search(array,target,0,len(array)-1)


    #중간점의 값보다 찾고자하는 값이 작은경우, - 왼쪽 확인
    elif array[mid] > target:
        return binary_search(array,target,start,mid-1)
    # 중간점의 값보다 찾고자 하는 값이 더 큰 경우 - 오른쪽 확인
    else:
        return binary_search(array,target,mid+1,end)


N,x = map(int,input().split())
arr = list(map(int,input().split()))
cnt = 0
binary_search(arr,x,0,len(arr)-1)
if cnt == 0:
    print(-1)
else:
    print(cnt)