import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(T):


    S = input()
    sstr = []
    iint = []
    for s in S:
        if int(ord(s)) >= 65:
            sstr.append(s)
        else:
            iint.append(int(s))

    sstr.sort()
    iiint = sum(iint)
    ans = ''.join(s for s in sstr) + str(iiint)
    print(ans)