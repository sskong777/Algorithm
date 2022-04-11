import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(T):
    S = input()

    sstr = []
    nnum = []
    for i in S:
        if i.isnumeric():
            nnum.append(int(i))
        else:
            sstr.append(i)
    sstr.sort()
    num = sum(nnum)

    res = ''.join(sstr) + str(num)
    print(res)
    # print(*sstr,end='',sep='')
    # print(num)