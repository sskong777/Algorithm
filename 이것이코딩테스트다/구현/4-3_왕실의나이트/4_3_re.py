import sys
sys.stdin  = open('input.txt', 'r')

iin = input()
row = ord(iin[0]) - 96
col = int(iin[1])

ans = 0

for di,dj in ((-2,-1),(-2,1),(2,1),(2,-1),(1,-2),(-1,-2),(1,2),(-1,-2)):
    nr, nc = row+di, col+dj
    if 1<=nr<=8 and 1<=nc<=8:
        ans +=1

print(ans)
