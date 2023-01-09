ssum = 0
for i in range(5):
    score = int(input())
    if score < 40:
        score = 40
    ssum += score
ans = ssum // 5
print(ans)