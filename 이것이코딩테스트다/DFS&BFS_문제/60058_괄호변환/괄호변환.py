def is_vaild(arr):
    stack = []
    for s in arr:
        # stack이 비어있을 때
        if not stack:
            if s == '(':
                stack.append(s)
            else:
                return stack
        elif s == '(':
            stack.append(s)
        elif s == ')':
            stack.pop()
    if not stack:
        return True
    else:
        return stack

def seperate(arr):
    pass
p = list(input())
# print(p)
if is_vaild(p) is True:
    print("올바른 괄호 문자열 입니다.")
else:
    print(is_vaild(p))
    # print(stack)