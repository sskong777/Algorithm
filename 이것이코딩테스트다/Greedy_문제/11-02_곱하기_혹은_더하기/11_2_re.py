import sys
sys.stdin = open('input.txt', 'r')

S = list(input())
# print(S)

ans = int(S[0])
for i in range(1, len(S)):
    if int(S[i]) ==0 or int(S[i]) == 1:
        ans += int(S[i])
    else:
        ans *= int(S[i])
print(ans)
