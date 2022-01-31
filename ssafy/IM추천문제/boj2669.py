
# 중복된 값을 제거해주기 위해 set 사용
field = set()
for num in range(4):
    # x,y좌표 입력받기
    x1, y1, x2, y2 = map(int, input().split())

    for x in range(x1, x2):
        for y in range(y1, y2):
            field.add((x, y))

print(len(field))