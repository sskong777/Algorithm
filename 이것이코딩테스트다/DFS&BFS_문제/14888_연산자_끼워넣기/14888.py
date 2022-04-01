from itertools import permutations
N = int(input())
num = list(map(int,input().split()))
oper = list(map(int,input().split()))

mmax = -1000000000
mmin = 1000000000
oper_lst = []

# 연산자 리스트로 넣어주기.
for i in range(len(oper)):
    if i == 0:
        for j in range(oper[i]):
            oper_lst.append("+")
    elif i == 1:
        for j in range(oper[i]):
            oper_lst.append("-")
    elif i == 2:
        for j in range(oper[i]):
            oper_lst.append("*")
    elif i == 3:
        for j in range(oper[i]):
            oper_lst.append("%")
oper_com = permutations(oper_lst,len(oper_lst))

# 순열로 나올 수 있는 경우를 다 계산
for i in oper_com:
    ssum = num[0]

    for j in range(1,N):
        if i[j-1] == '+':
            ssum += num[j]
        elif i[j - 1] == '-':
            ssum -= num[j]
        if i[j - 1] == '*':
            ssum *= num[j]
        if i[j - 1] == '%':
            ssum = int(ssum/num[j])
    # print(ssum)
    if ssum > mmax:
        mmax = ssum
    if ssum < mmin:
        mmin = ssum
print(mmax)
print(mmin)