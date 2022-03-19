N = int(input())
arr = [int(input()) for i in range(N)]


# # 1. 산술 평균
print(round(sum(arr)/N))



# # 2. 중앙값
arr2 = sorted(arr)
print(arr2[N//2])



# 3. 최빈값
counts = [0] * (4000*2 + 1)
for i in range(N):
    counts[4000+arr[i]] += 1

# 최빈값 개수와 최빈값에 해당하는 인덱스 배열 만들기
mode = []
max_counts = max(counts)
for i in range(len(counts)):
    if counts[i] == max_counts:
        mode.append(i)
mode.sort()
# print(mode)
# 최빈값이 하나일 때
if len(mode) == 1:
    print(mode[0]-4000)
# 최빈값이 두개일 때
else:
    print(mode[1]-4000)



# 4. 범위
print(max(arr) -min(arr))