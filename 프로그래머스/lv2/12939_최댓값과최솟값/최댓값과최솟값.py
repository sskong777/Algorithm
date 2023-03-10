def solution(s):
    arr = list(map(int,s.split()))
    # print(arr)
    mmin = min(arr)
    mmax = max(arr)
    answer = str(mmin) + ' ' + str(mmax)
    return answer