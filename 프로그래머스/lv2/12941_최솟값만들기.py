def solution(A, B):
    ans1 = 0
    Asort1 = sorted(A)
    Bsort1 = sorted(B, reverse=True)

    ans2 = 0
    Asort2 = sorted(A, reverse=True)
    Bsort2 = sorted(B)

    llen = len(A)

    for i in range(llen):
        ans1 += Asort1[i] * Bsort1[i]
        ans2 += Asort2[i] * Bsort2[i]

    answer = min(ans1, ans2)
    return answer