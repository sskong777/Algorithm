import sys
sys.stdin = open('input.txt', 'r')

# 1. selection sort
# T = int(input())
# for tc in range(1,T+1):
#     tn, leng = input().split()
#     arr = list(input().split())
#     # ["TWO NIN TWO TWO FIV FOR"]
#     num_eng = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
#     for i in range(leng):
#         for j in range(i+1, leng):
#             for num in range(len(num_eng)):
#                 if arr[i] == num_eng[num]:
#                     n1 = num
#                 if arr[j] == num_eng[num]:
#                     n2 = num
#             if n1 > n2 :
#                 arr[i], arr[j] = arr[j], arr[i]
#     print("#{}".format(tc))
#     print(*arr)

# 2.
T = int(input())
for tc in range(1,T+1):
    tn, leng = input().split()
    arr = list(input().split())
    num_eng = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    count = [0] * 10
    for i in range(len(arr)):
        for num in range(len(num_eng)):
                if arr[i] == num_eng[num]:
                    count[num] += 1
    print("#{}".format(tc))
    for i in range(len(count)):
        for j in range(count[i]):
            print(num_eng[i], end= ' ')
    print()