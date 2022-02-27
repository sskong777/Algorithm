import sys
sys.stdin = open('input.txt', 'r')
# 1. 재귀함수
# def func1(s):
#     if len(s) == 0:
#         return 0
#     elif len(s) > 1:
#         for i in range(len(s)):
#             if s[i-1] == s[i]:
#                 s = s.replace(s[i-1:i],'')
#                 return func1(s)
#     else:
#         return s


# 2. stack
def func2(s):
    stack = []
    for i in s:
        if stack and i == stack[-1]:
            stack.pop()
        else:
            stack.append(i)
    return stack

T = int(input())
for tc in range(1,T+1):
    s = input()
    res = len(func2(s))
    print("#{} {}".format(tc,res))