# 방법 1
n=int(input())
a=[list(map(int, input().split())) for _ in range(n)]
largest=-2147000000
for i in range(n):
    sum1=sum2=0
    for j in range(n):
        sum1+=a[i][j]
        sum2+=a[j][i]
    if sum1>largest:
        largest=sum1
    if sum2>largest:
        largest=sum2
sum1=sum2=0
for i in range(n):
    sum1+=a[i][i]
    sum2+=a[i][n-i-1]
if sum1>largest:
    largest=sum1
if sum2>largest:
    largest=sum2
print(largest)


# 방법 2
n=int(input())
arr=[list(map(int, input().split())) for _ in range(n)]
zip_arr = list(map(list, zip(*arr)))
row_sum = 0
col_sum = 0
for i in range(n):
    row_sum = max(row_sum,sum(arr[i]))
    col_sum = max(col_sum,sum(zip_arr[i]))

dia_sum = 0
reversed_dia_sum = 0
for i in range(n):
    dia_sum += arr[i][i]
    reversed_dia_sum += zip_arr[i][i]
print(max(row_sum,col_sum,dia_sum,reversed_dia_sum))
