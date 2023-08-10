import time

start_time = time.time()
N = int(input())
answer = 0
arr = list(map(int,list(input())))
answer = sum(arr)
print(answer)
print(time.time() - start_time)

# 1.6122732162475586


# start_time = time.time()
# n = int(input())
# numbers = list(input())
# sum = 0
#
# for i in numbers:
#     sum += int(i)
#
# print(sum)
# print(time.time() - start_time)
# 4.031641960144043
