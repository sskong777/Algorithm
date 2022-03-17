import sys
sys.stdin = open('input.txt', 'r')
isp = {'*' : 2, '+' : 1, '(' : 0} # 스택 안에서
icp = {'*' : 2, '+' : 1, '(' : 3} # 스택 밖에서

for tc in range(1,11):
    N = int(input())
    string = input()
    res = []
    stack = []
    for s in string:
        if s.isdigit():
            res.append(s)
        else:
            if not stack:
                stack.append(s)
                # continue
            elif stack:
                if s == ')':
                    while stack[-1] != '(':
                        res.append(stack.pop())
                    stack.pop() # ( 버리기

                elif icp[s] > isp[stack[-1]]:
                    stack.append(s)

                else:
                    while stack and icp[s] <= isp[stack[-1]]:
                        res.append(stack.pop())
                    stack.append(s)
            else:
                stack.append(s)
    while stack:
        res.append(stack.pop())


    cal_stack = []
    for r in res:
        if r.isdigit():
            cal_stack.append(int(r))
        else:
            second = cal_stack.pop()
            first = cal_stack.pop()
            if r == '*':
                cal_stack.append(first * second)
            elif r =='+':
                cal_stack.append(first + second)
    result = cal_stack[-1]
    print("#{} {}".format(tc,result))









    # while stack:
    #     res += stack.pop()

        # elif isp[s] >= stack[-1] and s == '+':
        #     stack.append(s)
        # elif isp[s] >= stack[-1] and s == '*':
        #     stack.append(s)
        #
        # elif s == '(':
        #     stack.append(s)
        # elif s == ')':
        #     while stack and stack[-1] == '(':
        #         res += stack.pop()
