x, y, w, h = map(int,input().split())
ga = [x, w-x]
se = [y, h-y]
res = min(min(ga),min(se))
print(res)