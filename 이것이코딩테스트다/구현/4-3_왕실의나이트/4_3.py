knight = input()

i = ord(knight[0])-97
j = int(knight[1])-1
# print(i,j)
cnt = 0
for di,dj in [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]:
    ni, nj = i+di,j+dj
    if 0<=ni<8 and 0<=nj<8:
        cnt += 1
print(cnt)