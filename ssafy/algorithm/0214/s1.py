import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
dr = [0, 1, 0, -1]
dc = [-1, 0, 1, 0]
for tc in range(1,N+1):
    total = 0

    arr = []
    n = int(input())
    for _ in range(n):
        arr.append(list(map(int, input().split())))
    for c in range(n):
        for r in range(n):
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if 0<= nr < n and 0 <= nc < n:
                    total += abs(arr[c][r] - arr[nc][nr])

    print("#{} {}".format(tc,total))