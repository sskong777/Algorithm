# https://programmers.co.kr/learn/courses/30/lessons/42889?language=python3
import sys
sys.stdin = open('input_14_25.txt', 'r')

def solution(N, stages):
    arr = []
    users = len(stages)
    for i in range(1,N+1):
        # count : 스테이지에 도달하지 못한 사람 수
        count = stages.count(i)
        if count == 0:
            fail = 0
        else:
            fail = count/users
        arr.append((i,fail))
        users -= count

        answer = sorted(arr, key=lambda x:-x[1])
        answer = [i[0] for i in answer]
    return answer

N = int(input())
stages = list(map(int,input().split()))

sol = solution(N,stages)
print(sol)

