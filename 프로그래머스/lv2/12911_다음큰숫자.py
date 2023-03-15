def solution(n):
    answer = n
    onecnt = bin(n).count('1')              # N의 2의진수의 1의 갯수

    while True:                             # 무한반복
        answer += 1
        answercnt = bin(answer).count('1')
        if answercnt == onecnt:
            break
    return answer