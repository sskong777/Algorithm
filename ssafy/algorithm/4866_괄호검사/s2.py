import sys
sys.stdin = open('input.txt', 'r')

def check_bracket(sen):
    stack = []
    # bracket = ['(', ')', '{', '}']
    for s in sen:
        if s =='(' or s == '{':
            stack.append(s)
        elif s ==')' or s =='}':
            if not stack:
                stack.append(s)
                break
            if stack[-1] == '(' and s ==')':
                stack.pop()
            elif stack[-1] == '{' and s =='}':
                stack.pop()
            else:
                break

    if stack:
        return 0
    return 1

T= int(input())
for tc in range(1,T+1):
    sen = input()
    check = check_bracket(sen)
    print("#{} {}".format(tc,check))

