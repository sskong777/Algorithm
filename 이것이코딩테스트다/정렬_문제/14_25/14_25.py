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
sort_stages = sorted(stages)
dict =  {}
for i in range(1,N+1):
    # clear : 스테이지에 도달한 플레이어 수
    clear = 0
    not_clear = 0
    for j in sort_stages:
        if i <= j:
            clear += 1
        if i == j:
            not_clear += 1
    dict[i] = not_clear/clear
sort_dict = sorted(dict.items(), key=lambda x : x[1], reverse=True)
res = []
for i in sort_dict:
    res.append(i[0])
print(res)
