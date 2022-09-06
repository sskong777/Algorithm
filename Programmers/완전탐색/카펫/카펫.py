# 조건1. x >= y
# 조건2. (x-2) * (y-2) = yellow
# 조건3. 2*x + 2*y -4 = brown

def solution(brown, yellow):
    rec_size = brown + yellow
    for y in range(1,rec_size+1):
        if (rec_size / y) % 1 == 0:          # 나누어 떨어질 때
            x = rec_size / y
            if x >= y:
                if 2*x + 2*y == brown + 4:
                    return [int(x),int(y)]

print(solution(24,24))