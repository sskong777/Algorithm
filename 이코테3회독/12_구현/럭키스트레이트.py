# 123402
def solution(input):
    arr = list(map(int,input))
    N = len(arr)//2

    if sum(arr[:N]) == sum(arr[N:]):
        return "LUCKY"
    else:
        return "READY"


print(solution("123402"))