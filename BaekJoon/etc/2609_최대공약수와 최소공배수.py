A,B = map(int,input().split())

g = 1   # 최대공약수
if A > B:    # 최소공배수
    l = A
    g = B
else:
    l = B
    g = A


while True:
    if A % g == 0 and B % g ==0:
        break
    g -= 1

while True:
    if l % A ==0 and l % B == 0:
        break
    l  += 1

print(g)
print(l)