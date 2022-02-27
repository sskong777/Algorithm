import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1,11):
    stack = []
    n, arr = input().split()
    # print(arr)
    for i in arr:
        # stack이 비어있지 않고 i가 스택의 마지막 값이랑 같다면
        if stack and i == stack[-1]:
            stack.pop()
        else:
            stack.append(i)
    print("#{}".format(tc), end=' ')
    print(''.join(map(str,stack)))
