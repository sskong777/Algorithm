#선택정렬(Selection Sort)
numbers = [12,21,4,43,13,45,76,93,54,84,23,46,2,57,88,74]

for i in range(0, len(numbers)-1):
    for j in range(i,len(numbers)):
        if numbers[i] > numbers[j]:
            temp = numbers[i]
            numbers[i] = numbers[j]
            numbers[j] = temp
print(numbers)




# 선택정렬 함수 구현
def selection_sort(nums):
    # 마지막 요소는 원소가 1개 있으니 정렬 할 필요가 없음
    for i in range(len(nums) - 1):
        # 최솟값에 해당하는 index를 i부터 시작 (0번 위치가 기준위치가 된다.)
        min_idx = i
        # i 다음부터 보자 (i부터하면 한번 더 보게된다.)
        for j in range(i + 1, len(nums)):
            # 내가 가진 최솟값(min_idx)보다 더 작다?
            # 큰걸 뒤로 보낸다는 느낌으로!
            if nums[min_idx] > nums[j]:
                # 인덱스 갱신
                min_idx = j
        # i번째와 min_idx 위치를 교환한다.
        # 교환은 마지막에 한번 일어남
        nums[i], nums[min_idx] = nums[min_idx], nums[i]


def selectionsort(arr):
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                arr[i],arr[j] = arr[j],arr[i]

arr = [5,21,23,23,87,2,3,45,9,4,8,0,12,1,4,56]
selectionsort(arr)
print(arr)
selection_sort(arr)
print(arr)