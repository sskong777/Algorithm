N = int(input())
pick = list(map(int, input().split()))

line = []
for i in range(N):
    line.insert(i-pick[i], i+1)

# join의 인자는 str로 이루어진 리스트이어야한다. --> int로 이루어진 리스트를 넣으면 에러발생.
# print(' '.join(map(str,line)))
print(*line)
