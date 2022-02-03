n1, n2 = input().split()
r1, r2 = '', ''
for i in range(len(n1)-1,-1,-1):
    r1 += n1[i]
    r2 += n2[i]

if int(r1) > int(r2):
    print(int(r1))
else:
    print(int(r2))

