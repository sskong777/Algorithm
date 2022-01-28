
num = int(input())
li1 = []
for i in range(1,num+1):
    ans = []
    ans.append(num)
    ans.append(i)

    i = 2
    while True:
        ans.append(ans[i-2] - ans[i-1])
        i += 1
        if ans[i-2] - ans[i-1] < 0:
            break
    li1.append(ans)

max = 0
for i in range(len(li1)):
    if len(li1[i]) > max:
         max = len(li1[i])
         ans_idx = i
print(max)
print(*li1[ans_idx])
    