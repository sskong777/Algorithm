c = int(input())

res = []
for i in range(c):

    score_li = list(map(int, input().split()))
    sum = 0
    for i in range(1,len(score_li)):
        sum += score_li[i]
    
    avg = sum/score_li[0]

    cnt = 0
    for i in score_li[1:]:
        if i > avg:
            cnt += 1
    res.append(cnt/score_li[0]* 100)


for i in res:
    print("{:.3f}%".format(i))