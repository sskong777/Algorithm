# # 1.
# import sys
# sys.stdin = open('input.txt', 'r')
# for tc in range(1,11):
#     n = int(input())
#     arr = list(map(int, input().split()))
#     # print(arr)
#     res = 1
#     while res != 0:
#         for i in range(1, 6):
#             a = arr.pop(0) - i
#             if a <= 0:
#                 a = 0
#                 arr.append(a)
#                 res = 0
#                 break       # 중요
#             else:
#                 arr.append(a)
#
#     print("#{}".format(n), end=' ')
#     print(*arr)


# 2.
# import sys
# sys.stdin = open('input.txt', 'r')
# for tc in range(1, 11):
#     n = int(input())
#     arr = list(map(int, input().split()))
#     # print(arr)
#     res = 1
#     while res != 0:
#         for i in range(1, 6):
#             a = arr.pop(0)
#             arr.append(a - i)
#
#             if arr[-1] <= 0:
#                 arr[-1] = 0
#                 res = 0
#                 break
#
#     print("#{}".format(n), end='')
#     print(*arr)

# 3.
# def func1(arr):
#     if arr[-1] <= 0:
#         arr[-1] = 0
#         return arr

#     for i in range(1, 6):
#         a = arr.pop(0)
#         arr.append(a - i)
#     func1(arr)
#
#
# import sys
# sys.stdin = open('input.txt', 'r')
# for tc in range(1,11):
#     n = int(input())
#     arr = list(map(int, input().split()))
#
#     res = func1(arr)
#     print(* res)
