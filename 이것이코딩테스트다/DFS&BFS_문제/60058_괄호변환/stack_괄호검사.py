# 괄호검사
def check(arr):
    stack = []
    for s in arr:
        if not stack:
            if s == '(':
                stack.append(s)
            else:
                return False
        elif s == '(':
            stack.append(s)
        elif s == ')':
            stack.pop()
    if not stack:
        return True
    return False


arr = input()
res = check(arr)
print(res)