import math
A, B, V = map(int,input().split())
res = (V - B) / (A-B)
print(math.ceil(res))

