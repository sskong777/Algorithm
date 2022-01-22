a = int(input())
b = int(input())
c = int(input())

multi = list(str(a * b * c))

# res = [0] * 10
# for i in multi:
#     for j in range(0,10):
#         if int(i) == j:
#             res[j] += 1

# for i in range(len(res)):
#     print(res[i])


for i in range(10):
    print(multi.count(str(i)))