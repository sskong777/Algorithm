import sys
sys.stdin = open('input.txt', 'r')

# 분할과정
def merge_sort(arr):
    if len(arr) <= 1:
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
    global cnt,N
    # 계속해서 왼쪽의 첫번째 값과 오른쪽의 첫번째값을 비교하여 작은 값을 result에 담아주는 방식
    result = [0] * N
    left_len = len(left)
    right_len = len(right)
    left_i,right_i = 0,0
    i = 0
    # 문제 조건
    if left[-1] > right[-1]:
        cnt += 1
    # 왼쪽,오른쪽 리스트중 하나라도 비어있지 않을 때 까지 반복
    while left_i < left_len or right_i < right_len:
        # 왼쪽과 오른쪽 리스트 둘 다 비어 있지 않다면
        if left_i < left_len and right_i < right_len:
            # 왼쪽리스트의 첫번째 값이 오른쪽 리스트의 첫번째 값보다 작다면
            if left[left_i] <= right[right_i]:
                # result에 왼쪽리스트의 첫번째 값을 넣어주고, 왼쪽리스트의 첫번째 값은 제거해준다
                result[i] = left[left_i]
                i += 1
                left_i += 1
            else:
                result[i] = right[right_i]
                i += 1
                right_i += 1
        # 합병 중 왼쪽 리스트만 남아있을 경우 왼쪽리스트를 result에 담아줌
        elif left_i < left_len:
            result[i] = left[left_i]
            i += 1
            left_i += 1
        elif right_i < right_len:
            result[i] = right[right_i]
            i += 1
            right_i += 1
    return result

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = list(map(int,input().split()))
    cnt = 0
    res = merge_sort(arr)

    print(f'#{tc} {res[N//2]} {cnt}')