import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1,T+1):
    stack = []
    line = input().split()
    res ='error'
    for i in line:
        # if i in '0123456789' or i =='10':
        #     stack.append(int(i))
        if i.isdigit():
            stack.append(int(i))

        elif len(stack) >= 2 and i =='+':
            second = stack.pop()
            first = stack.pop()
            stack.append((first + second))

        elif len(stack) >= 2 and i == '*':
            second = stack.pop()
            first = stack.pop()
            stack.append((first * second))

        elif len(stack) >= 2 and i == '-':
            second = stack.pop()
            first = stack.pop()
            stack.append((first - second))

        elif len(stack) >= 2 and i == '/':
            second = stack.pop()
            first = stack.pop()
            stack.append((first // second))
            # if second == 0:
            #     res = 'error'
            #     break
        elif i =='.' and len(stack) == 1:
            res = stack[-1]
            # break
        else:
            res = 'error'
            break

    print("#{} {}".format(tc,res))