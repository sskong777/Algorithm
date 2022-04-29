# deque이용
from collections import deque

import sys
sys.stdin = open('input.txt')

N,K = map(int,input().split())
q = [i for i in range(1,N+1)]
res = []

while q:
    for i in range(K-1):
        q.append(q.pop(0))
    res.append(q.pop(0))
print('<',end='')
print(*res,sep=', ',end='')
print(">")
