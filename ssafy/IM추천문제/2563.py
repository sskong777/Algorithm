N = int(input())
field = set()
for n in range(N):
    r,c = map(int,input().split())
    for x in range(r,r+10):
        for y in range(c, c+10):
            field.add((x,y))
print(len(field))