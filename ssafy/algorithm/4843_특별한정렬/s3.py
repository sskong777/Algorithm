import sys
sys.stdin = open('input.txt', 'r')

def special_sort(n,arr):
    start = 0
    end = len(arr)-1
    arr2 = [0] * len(arr)
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

    for i in range(0, len(arr), 2):
        # print(arr)
        arr2[i] = arr[end]
        arr2[i+1] = arr[start]
        start += 1
        end -= 1
        res = arr2[:10]
    return ' '.join(map(str,res))
    # return res

T = int(input())
for tc in range(1,T+1):
    n = int(input())
    arr = list(map(int, input().split()))
    print("#{} {}".format(tc, special_sort(n,arr)))






# n = 20
# arr = [3, 69, 21, 46, 43, 60, 62, 97, 64, 30, 17, 88, 18, 98, 71, 75, 59, 36, 9, 26]
# print(special_sort(n, arr))




