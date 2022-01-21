# 빠른 A+B 
# sys.stdin.readline

import sys

T = int(sys.stdin.readline())

for i in range(T):
    a, b = map(int, sys.stdin.readline().split())

    print(a + b)