arr = [3,6,7,1,5,4]
N = len(arr)

data = []
for i in range(1<<N):    # 부분집합의 갯수
    a = []
    for j in range(N):      # 원소의 수 만큼 비트 비교
        if i & (1<<j):  #i의j번째 비트가 1이면 j번째 원소 출력
            a.append(arr[j])
    data.append(a)
print(data)
