import sys
sys.stdin = open('input.txt', 'r')

def bfs(s):
    pass
    q = []
    v = [0] * 101
    q.append(s)
    v[s] = 1
    sol = s

    while q:
        c = q.pop(0)
        if v[sol] < v[c] or (v[sol]==v[c] and sol<c):
            sol = c

        for j in range(1,101):
            if adj[c][j] and v[j] == 0:
                q.append(j)
                v[j] = v[c] + 1
    return sol


T = 10
for tc in range(1,T+1):
    N,S = map(int,input().split())
    arr = list(map(int,input().split()))
    # 인접 행렬
    adj = [[0]*101 for _ in range(101)]
    for i in range(0,len(arr),2):
        adj[arr[i]][arr[i+1]] = 1

    ans = bfs(S)
    print(f'#{tc} {ans}')