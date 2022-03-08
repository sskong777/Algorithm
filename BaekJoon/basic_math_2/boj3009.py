rec_x = []
rec_y = []

ans_x = 0
ans_y = 0
for i in range(3):
    x, y = map(int,input().split())
    rec_x.append(x)
    rec_y.append(y)
for i in rec_x:
    if rec_x.count(i) == 1:
        ans_x = i
for i in rec_y:
    if rec_y.count(i) == 1:
        ans_y = i
print(ans_x, ans_y)