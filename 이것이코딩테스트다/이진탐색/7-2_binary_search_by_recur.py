def binary_search(array,target,start,end):
    if start > end:
        return
    mid = (start+end)//2

    if array[mid] == target:
        return mid

    #중간점의 값보다 찾고자하는 값이 작은경우, - 왼쪽 확인
    elif array[mid] > target:
        return binary_search(array,target,start,mid-1)
    # 중간점의 값보다 찾고자 하는 값이 더 큰 경우 - 오른쪽 확인
    else:
        return binary_search(array,target,mid+1,end)


n, target = list(map(int,input().split()))
array = list(map(int,input().split()))

result = binary_search(array,target,0,n-1)

if not result:
    print('원소가 존재하지 않습니다')
else:
    print(result+1)     # 인덱스 값이므로 1 더해준다

