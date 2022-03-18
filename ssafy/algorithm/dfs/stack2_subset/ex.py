import sys
sys.stdin = open('input.txt', 'r')

# 부분집합의 합 (stack2 연습문제) -DFS로 풀이

def dfs(n,ssum):
    global sol
    if n ==N:
        if ssum == K:
            sol += 1
        return

    dfs(n+1,ssum+arr[n])
    dfs(n+1,ssum)

T = int(input())
for tc in range(1,T+1):
    N ,K = map(int,input().split())
    arr = list(map(int,input().split()))
    sol = 0
    dfs(0,0)
    print(f'#{tc} {sol}')