
word = input()
ans = [-1] * 26
for i in range(ord('a'),ord('z')+1):
    if chr(i) in word:
        ans[i-97] = word.index(chr(i))

for i in ans:
    print(i,end=' ')