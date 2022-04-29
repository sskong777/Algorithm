import sys
sys.stdin = open('input.txt')

def dp(N):
    d = [0] * 251
    d[0] = 1
    d[1] = 1
    d[2] = 3
    # N = int(input())
    for i in range(3, N + 1):
        d[i] = d[i - 1] + 2 * d[i - 2]
    return d[N]

while True:
    try:
        print(dp(int(input())))
    except:
        break