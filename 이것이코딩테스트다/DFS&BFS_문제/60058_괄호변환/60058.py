import sys
sys.stdin = open('input.txt', 'r')

def seperate(p):
    u,v = '',''
    cnt = [0,0]
    for i in range(len(p)):
        if p[i] =='(':
            cnt[0] += 1
        else:
            cnt[1] += 1

        if cnt[0] == cnt[1]:
            u = p[:i+1]
            v = p[i+1:]
            break
    return u,v

def is_vaild(p):
    stack = 0
    for i in range(len(p)):
        if p[i] =='(':
            stack += 1
        else:
            if stack:
                stack -= 1
            else:
                return False
    return True

def p_flip(p):
    new_p = ''
    for i in range(len(p)):
        if p[i] == '(':
            new_p += ')'
        else:
            new_p += '('
    return new_p


def solution(p):
    if p:
        u,v = seperate(p)

        if is_vaild(u):
            return u + solution(v)
        else:
            new_p = '('

            new_p += solution(v)

            new_p += ')'

            new_p += p_flip(u[1:-1])

            return new_p
    else:
        return ''


T = int(input())
for tc in range(1,T+1):
    p = input()

    res = solution(p)
    print(res)