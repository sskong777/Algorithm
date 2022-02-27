def make_lps(P):
    len_p = len(P)
    lps = [0] * len_p

    lps[0] = -1  # 의미
    s = 0   # 몇 번째까지 패턴인지

    for p_idx in range(1, len_p):
        lps[p_idx] = s  # 현재 패턴의 위치에 이전의 s 값 대입
        # if P[p_idx] == P[s]:
        #     s += 1
        # else:
        while s > 0 and P[p_idx] != P[s]: # 이전 패턴들과 같지 않으면 계속 비교
            s = lps[s]                    # 디버거로 꼭 살펴보긔!!!!

        if P[p_idx] == P[s]:
            s += 1

    return lps


import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    P = input()

    lps = make_lps(P)
    print(f'#{tc} {lps}')