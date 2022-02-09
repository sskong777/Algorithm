word = input()
rep = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=',
       'z=']
for i in range(len(rep)):
    word = word.replace(rep[i],"*")

print(len(word))

# 방법 2.

# str1 = input()
# count = 0
# # 1. -, = 제거하기
# rem = ['-', '=']
# for r in rem:
#     str1 = str1.replace(r,"")
# # print(str1)
#
# # 문자열 묶기
# str2 = ['dz', 'lj', 'nj']
# # print(str1[0:1])
# for i in range(len(str1)):
#     if str1[i:i+2] in str2:
#         continue
#     else:
#         count += 1
#
# print(count)