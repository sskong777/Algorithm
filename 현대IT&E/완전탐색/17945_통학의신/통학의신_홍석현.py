A, B = map(int,input().split())

answer1 = int(-A + (A**2 - B)**0.5)
answer2 = int(-A - (A**2 - B)**0.5)

if answer1 == answer2:
    print(answer1)
else:
    print(answer2, answer1)
