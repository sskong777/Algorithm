import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(T):
    ps = input()


    stack = []
    flag = True
    for s in ps:
        if s=='(':
            stack.append(s)
        else:
            if stack:
                stack.pop()

            else:
                flag = False
                break

    if not stack and flag==True:
        print("YES")
    else:
        print("NO")
