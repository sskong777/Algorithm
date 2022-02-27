import sys
sys.stdin = open('input.txt')

def brute_force_for(p, t):
    # target-pattern+1 길이
    for i in range(len(t) - len(p) + 1):
        # pattern 길이
        for j in range(len(p)):
            if t[i + j] != p[j]:
                break
        else:
            return 1
    return 0


def brute_force_while(p, t):
    i = 0  # text를 컨트롤 하는 인덱스
    j = 0  # pattern을 컨트롤 하는 인덱스

    # i가 text의 길이가 된다면 -> 찾았다! -> 멈추자!
    # j가 pattern의 길이가 된다면 -> 찾았다! -> 멈추자!
    while j < len(p) and i < len(t):
        if p[j] != t[i]:
            # 시작 위치로 돌아감
            i = i - j
            # 밑에서 첫 인덱스로 돌아가기 위함
            j = -1
        # 시작 위치에서 +1
        i += 1
        # 첫 인덱스로 돌아옴
        j += 1

    # pattern의 길이와 pattern을 체크하는 인덱스(j)가 같아지면 회문을 찾은 것
    if j == len(p):
        return 1
    else:
        return 0


T = int(input())
for tc in range(1, T + 1):
    pattern = input()
    target = input()
    # result = brute_force_for(pattern, target)
    result = brute_force_while(pattern, target)
    print('#{} {}'.format(tc, result))