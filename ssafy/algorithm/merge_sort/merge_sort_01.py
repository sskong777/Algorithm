# 분할과정
def merge_sort(arr):
    if len(arr) == 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)
    # arr 리스트들을 길이가 1이 될때까지 반복하여 나누어준뒤, merge함수를 호출한다.
    return merge(left,right)

# 합병과정
def merge(left, right):
    # 계속해서 왼쪽의 첫번째 값과 오른쪽의 첫번째값을 비교하여 작은 값을 result에 담아주는 방식
    result = []
    # 왼쪽,오른쪽 리스트중 하나라도 비어있지 않을 때 까지 반복
    while len(left) > 0 or len(right) > 0:
        # 왼쪽과 오른쪽 리스트 둘 다 비어 있지 않다면
        if len(left) > 0 and len(right) > 0:
            # 왼쪽리스트의 첫번째 값이 오른쪽 리스트의 첫번째 값보다 작다면
            if left[0] <= right[0]:
                # result에 왼쪽리스트의 첫번째 값을 넣어주고, 왼쪽리스트의 첫번째 값은 제거해준다
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
        # 합병 중 왼쪽 리스트만 남아있을 경우 왼쪽리스트를 result에 담아줌
        elif len(left) > 0:
            result.append(left.pop(0))
        elif len(right) > 0:
            result.append(right.pop(0))
    return result

arr = [14,7,3,12,9,11,6,2]

res = merge_sort(arr)
print(res)