# append, pop, sort를 사용
# heapq를 사용했을 때와 비교하여 시간 효율이 좋지 않을 것 같다.

def solution(operations):
    answer = []

    for i in operations:
        a, b = i.split()
        if a == 'I':
            answer.append(int(b))
        else:
            if len(answer) > 0:
                if b == '1':
                    answer.pop()
                else:
                    answer.pop(0)
            else:
                pass
        answer.sort()

    if len(answer) == 0:
        return [0, 0]
    else:
        return [max(answer), min(answer)]