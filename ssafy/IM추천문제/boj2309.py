import random
# li = []
# for i in range(7):
#     a = random.randint(0,9)
#     if a in li:
#         i -= 1
#     else:
#         li.append(a)
import random
index = random.sample(range(0, 10), 7)  # 1부터 100까지의 범위중에 10개를 중복없이 뽑겠다.
# print(index)

dwarf = []
for i in range(9):
    k = int(input())
    dwarf.append(k)
while True:
    ran_7 = random.sample(dwarf, 7)  # 1부터 100까지의 범위중에 10개를 중복없이 뽑겠다.
    res = sum(ran_7)
    if res == 100:
        break
for i in range(7):
    print(sorted(ran_7)[i])


