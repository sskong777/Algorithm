# 배열의 크기 : N
# 숫자가 더해지는 횟수 : M
# 연속으로 가능한 횟수  : K

# 5 8 3
# 2 4 5 4 6

sum = 0
count = 0
N,M,K = map(int,input('').split())
array = list(map(int,input('').split()))
array.sort(reverse=True)

max = array[0]
max2 = array[1]

while count < M:
    for j in range(K):
        sum += max
        count += 1
    sum += max2
    count += 1

print(sum)

