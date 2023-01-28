import sys
sys.stdin = open('input.txt', 'r')

from itertools import permutations

mmax = -1000000000
mmin = 1000000000

T = int(input())
for tc in range(T):

    N = int(input())
    arr = list(map(int,input().split()))
    operator = list(map(int,input().split()))

    oper_list = []
    for i in range(len(operator)):
        if i == 0:
            for j in range(operator[i]):
                oper_list.append('+')
        elif i == 1:
            for j in range(operator[i]):
                oper_list.append('-')
        elif i == 2:
            for j in range(operator[i]):
                oper_list.append('*')
        elif i == 3:
            for j in range(operator[i]):
                oper_list.append('%')

    oper = permutations(oper_list)
    for i in oper:
        ssum = arr[0]

        for j in range(1,N):
            if i[j-1] == '+':
                ssum += arr[j]
            elif i[j-1] =='-':
                ssum -= arr[j]
            elif i[j-1] =='*':
                ssum *= arr[j]
            elif i[j-1] =='%':
                ssum = int(ssum / arr[j])

        if ssum > mmax:
            mmax = ssum
        if ssum < mmin:
            mmin = ssum

    print(mmax)
    print(mmin)