N = int(input())
arr = []

for i in range(N):
    arr.append(input())

# 중복 제거
arr_set = set(arr)
arr_li = list(arr_set)

# 알파벳 순으로 정렬
arr_li.sort()

# 길이 순으로 정렬
arr_li.sort(key=len)

for i in range(len(arr_li)):
    print(arr_li[i])