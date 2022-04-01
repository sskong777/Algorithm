import sys
sys.stdin = open('input.txt', 'r')

def dfs(idx,cnt):
    global res

    # 버스가 끝까지 갈 수 있으면 종료
    if idx >= N-1:
        if cnt < res:
            res = cnt
        return

    # 가지치기(크거나 같다고 해야 시간초과가 안난다.)
    if cnt >= res:
        return

    # 해당인덱스(idx)에서 갈 수 있는 경우의 수를 반복문을 통해 dfs를 호출해준다.
    for i in range(1,arr[idx]+1):
        dfs(idx+i,cnt+1)

T = int(input())
for tc in range(1,T+1):
    N, *arr = map(int,input().split())

    res = 100
    dfs(0,-1)

    print(f'#{tc} {res}')
