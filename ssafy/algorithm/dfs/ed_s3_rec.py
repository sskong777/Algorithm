import sys
sys.stdin = open('input.txt', 'r')


def DFS(v):
    global visited, G, V
    # stack = [n]
    #
    # while len(stack):
    #     v = stack.pop()

    # if visited[v] == 0:
    visited[v] = 1
    # print(f'{v} {visited}')
    print(f'{v}', end=' ')

    for w in range(1, V + 1):
        if G[v][w] == 1 and visited[w] == 0:
            DFS(w)


V, E = map(int, input().split())
data = list(map(int, input().split()))

G = [[0 for _ in range(V + 1)] for _ in range(V + 1)]

visited = [0] * (V + 1)

for i in range(V + 1):
    '''
    G[data[0]][data[1]] = 1
    G[data[1]][data[0]] = 1

    G[data[2]][data[3]] = 1
    G[data[3]][data[2]] = 1
    '''
    G[data[i * 2]][data[i * 2 + 1]] = 1
    G[data[i * 2 + 1]][data[i * 2]] = 1

DFS(1)