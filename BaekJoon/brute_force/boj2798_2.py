def blackjack(N,M,cards):
    flag = True
    while flag:
        for i in range(N):
            for j in range(i + 1, N):
                for k in range(j + 1, N):
                    if cards[i] + cards[j] + cards[k] == M:
                        return M
        M -= 1


N, M = map(int,input().split())
cards = list(map(int,input().split()))

res = blackjack(N,M,cards)
print(res)