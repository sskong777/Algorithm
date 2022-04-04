import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1,T+1):
    N,E = map(int,input().split())
    # arr = [list(map(int,input().split())) for _ in range(E)]
    adj = [[0]*(N+1) for _ in range(N+1)]
    for i in range(E):
        s,e,w = map(int,input().split())
        adj[s][e] = w
    print(adj)
