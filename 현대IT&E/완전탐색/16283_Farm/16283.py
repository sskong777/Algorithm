import sys
sys.stdin = open('input.txt', 'r')

a, b, n, w = map(int,input().split())

sheeps = 1
goat = n - 1

answer = []
for i in range(n-1):
    if sheeps * a + goat * b == w:
        answer.append([sheeps, goat])
    sheeps += 1
    goat -= 1
if not answer or len(answer) > 1:
    print(-1)
else:
    print(answer[0][0], answer[0][1])

