def lps(P):
    len_p = len(P)
    lps = [0] * len_p

    lps[0] = -1
    s = 0
    for p_idx in range(1,len_p):
        lps[p_idx] = s  #
        # if P[p_idx] == P[s]:
        #     s += 1
        # else:
        #     while s > 0 and P[p_idx] != P[s]:
        #         s = lps[s]
        #
        #     if P[p_idx] == P[s]:
        #         s += 1

        while s > 0 and P[p_idx] != P[s]:
            s = lps[s]
            #
        if P[p_idx] == P[s]:
            s += 1

    return lps