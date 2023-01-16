import sys
sys.stdin = open('input.txt', 'r')

num = list(map(int, input()))
# print(num)

count_one = 0
count_zero = 0
for i in range(1, len(num)):
    if num[i - 1] != num[i]:
        if num[i] == 1:
            count_zero += 1
        else:
            count_one += 1

print(min(count_zero, count_one))
