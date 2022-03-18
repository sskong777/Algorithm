import sys
sys.stdin = open('input.txt','r')

def bfs(s):
    q = []
    v = [0]*101
    q.append(s)
    v[s] = 1
    sol = s

    while q:
        c = q.pop(0)
        if v[sol] < v[c] or v[sol]==v[c] and sol<c:
            sol = c

        for j in range(1,101):
            if adj[c][j] and v[j]==0:
                q.append(j)
                v[j] = v[c]+1
    return sol


T = 10
for tc in range(1,T+1):
    N,S = map(int,input().split())
    lst = list(map(int,input().split()))
    # lst 연결값을 인접행렬에 저장
    adj = [[0]*101 for _ in range(101)]
    for i in range(0,len(lst),2):
        adj[lst[i]][lst[i+1]] = 1


    ans = bfs(S)
    print(f'#{tc} {ans}')