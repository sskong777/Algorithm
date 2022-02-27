import sys
sys.stdin = open('input.txt', 'r')
# push & pop 함수 구현
def push(item, size):
    global top
    top += 1
    if top == size:
        print('overflow')
    else:
        stack[top] = item

def pop():
    global top
    if top == -1:
        print('underflow')
        return
    else:
        top -= 1
        return stack[top+1]


# # operators = ['+', '*']
# operators = {'+' : 1, '*' : 2}
#
# stack = []
# top = -1
#
# lst = []
# line = list(input())
# for i in line:
#     if i in operators:
#         stack.append(i)
#     else:
#         lst.append(int(i))

T = 10
for tc in range(1,T+1):
    N = int(input())
    line = input()

    stack = []
    res = ''

    for s in line:
        if s in '0123456789':
            res += s
        elif s == '*':
            stack.append(s)
        elif s == '+':
            while stack and stack[-1] == "*":
                res += stack.pop()
            stack.append(s)
    while stack:
        res += stack.pop()

    # print(res)

    # 계산할 때 사용할 스택
    cal_stack = []
    for c in res:   # 후위표기법에서 하나씩 읽어온다.
        if c in '0123456789':
            cal_stack.append(int(c))
        else:
            second = cal_stack.pop()
            first = cal_stack.pop()

            if c == '*':
                cal_stack.append((first*second))    # 계산된 결과를 다시 stack에 넣는다
            elif c == '+':
                cal_stack.append((first+second))
    result = cal_stack[-1]
    print(result)





