def f(a, N, key): # 배열, 배열의 크기, 키값
    start = 0
    end = N-1
    while start < end:
        middle = (start + end) // 2
        if a[middle] == key: # 검색 성공
            return middle
        elif a[middle] > key :
            end = middle -1
        else :
            start = middle + 1
    return -1 # 검색 실패

arr = [1,2,3,4,5,6,6,7,8,9,9,10]
f = f(arr,len(arr), 7)
print(f)