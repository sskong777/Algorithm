n = int(input())
arr = []
for _ in range(n):
    start,end = map(int,input().split())
    arr.append((start,end))
arr.sort(key=lambda x:(x[1],x[0]))  # 종료시간이 같으면 시작시간이 빠른 순으로 정렬

print(arr)
answer = 0

end_time = -1
for i in range(n):
    if arr[i][0] >= end_time:
        end_time = arr[i][1]
        answer += 1

print(answer)


# n = int(input())
# arr = [[0] * 2 for _ in range(n)]
#
# for i in range(n):
#     s,e = map(int,input().split())
#     arr[i][0] = e
#     arr[i][1] = s
# arr.sort()
# count = 0
# end = -1
#
# for i in range(n):
#     if arr[i][1] >= end:
#         end = arr[i][0]
#         count += 1
# print(count)