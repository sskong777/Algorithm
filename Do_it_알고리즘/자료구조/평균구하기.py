N = int(input())
arr = list(map(int,input().split()))
_sum = 0
_max = max(arr)
for i in arr:
    _sum += (i/_max)*100
print(_sum/N)

# N = 1000
# time = 2s => 40000000