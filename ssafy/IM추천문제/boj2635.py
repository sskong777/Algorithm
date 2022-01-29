num = int(input())
li1 = []
# num보다 큰 수가 두번째 수로 들어가면 음수이므로 1부터 num까지의 숫자로 for문을 돌린다.
for i in range(1,num+1):
    ans = []
    ans.append(num)
    ans.append(i)
		# 1부터 num까지 숫자가 두번째 숫자일 때 ans의 리스트를 구한뒤 li1리스트에 담아준다.
    i = 2
    while True:
        ans.append(ans[i-2] - ans[i-1])
        i += 1
        if ans[i-2] - ans[i-1] < 0:
            break
    li1.append(ans)
# li1리스트의 요소 중에서 리스트 길이가 가장 큰 값과 그 리스트의 인덱스를 찾아준다.
max = 0
for i in range(len(li1)):
    if len(li1[i]) > max:
         max = len(li1[i])
         ans_idx = i
# li1리스트의 가장 큰 길이와 그에 해당하는 ans리스트를 출력한다.
print(max)
print(*li1[ans_idx])