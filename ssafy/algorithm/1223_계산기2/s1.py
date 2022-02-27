import sys
sys.stdin = open('input.txt', 'r')

T = 10
for tc in range(1, T+1):
    N = int(input())
    string = input()

    stack = []
    res = ''

    for char in string:
        if char in '0123456789':
            res += char
        elif char == '*':
            stack.append(char)
        elif char == '+':
            while stack and stack[-1] == '*':
                res += stack.pop()
            stack.append(char)

    while stack:
        res += stack.pop()

    # 계산 할 때 사용할 스택
    cal_stack = []
    for c in res:   # 후위 표기법에서 하나씩 읽어 온다.
        if c in '0123456789':
            cal_stack.append(int(c))   # 계산을 위해 정수형으로 형 변환
        else:
            second = cal_stack.pop()
            first = cal_stack.pop()
            if c == '*':
                cal_stack.append(first * second)  # 계산된 결과를 다시 stack에 넣는다.
            elif c == '+':
                cal_stack.append(first + second)

    result = cal_stack[-1]
    print(f'#{tc} {result}')