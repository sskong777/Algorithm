def solution(s):
    stack = []
    for x in s:
        if x == '(':
            stack.append(x)
        else:  # x 가 ) 일때
            if stack:  # stack에 괄호가 남아있다면
                stack.pop()  # 짝을 이뤘으므로 ( 하나를 삭제
            else:  # )이면서 stack에 담긴것이 없으면 짝이 맞지 않으므로 False
                return False
    if stack:
        return False

    return True