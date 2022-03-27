import sys
sys.stdin = open('input_14_23.txt', 'r')

def chage_char(char):
    if char.isnumeric():
        return int(char)
    else:
        return char

N = int(input())
arr = []
for n in range(N):
    arr.append(list(map(chage_char,input().split())))

# sort와 lambda로 정렬
# (정렬할 우선순위를 튜플로 묶어서 사용할 수 있다.)
# 내림차순으로 정렬하고 싶으면 '-'를 붙이면 된다.
arr.sort(key=lambda x : (-x[1],x[2],-x[3],x[0]))

for i in arr:
    print(i[0])