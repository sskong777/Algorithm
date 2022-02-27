import sys
sys.stdin = open('input.txt', 'r')
def func1(N):
    global memo
    if N >= 2 and len(memo) <= N:
        memo.append(func1(N-1) + (func1(N-2) * 2))
    return memo[N]

memo = [1, 3]

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    print("#{} {}".format(tc,func1(N//10 -1)))
