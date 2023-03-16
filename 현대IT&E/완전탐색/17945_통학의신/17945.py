import sys
sys.stdin = open('input.txt', 'r')

import math
A, B = map(int,input().split())

answer1 = (-2*A + math.sqrt(4* A**2 - 4*B)) / 2
answer2 = (-2*A - math.sqrt(4* A**2 - 4*B)) / 2

answer = []
answer.append(int(answer1))
answer.append(int(answer2))
answer.sort()
answer = set(answer)
print(*answer)