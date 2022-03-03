find = int(input())
line = 0
last = 0
while find > last:
    line += 1
    last += line

if line % 2:       #line이 홀수 번째 라면
    a = 1 + (last-find)
    b = line - (last-find)
else:
    a = line - (last - find)
    b = 1 + (last - find)
print(str(a) + '/' +str(b))














# num = int(input())
# count = 1
# N = 2
# res = 0
# while res == 0:
#     if N % 2 == 0:
#         a = N-1
#         b = 1
#         for i in range(N-1):
#             if count == num:
#                 res = 1
#                 break
#             a -= 1
#             b += 1
#             count += 1
#
#     else:
#         a = 1
#         b = N-1
#         for i in range(N-1):
#             if count == num:
#                 res = 1
#                 break
#             a += 1
#             b -= 1
#             count += 1
#     N += 1
# print(a,b)