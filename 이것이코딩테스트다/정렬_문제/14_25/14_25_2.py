# https://programmers.co.kr/learn/courses/30/lessons/42889?language=python3
import sys
sys.stdin = open('input_14_25.txt', 'r')

def solution(N, stages):
    # fail_per
    sort_stages = sorted(stages)
    answer = []
    return answer


N = int(input())
stages = list(map(int,input().split()))

arr = []
for i in range(1,N+1):
    # clear : 스테이지에 도달한 플레이어 수
    clear = 0
    not_clear = 0
    for j in stages:
        if i <= j:
            clear += 1
        if i == j:
            not_clear += 1
    arr.append([i, not_clear/clear])

answer = [idx for idx, v in sorted(arr,key=lambda x: -x[-1])]
print(answer)