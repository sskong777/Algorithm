N = int(input())
# for i in range(N):
#     card = int(input())
cards = [int(input()) for _ in range(N)]
# print(cards)
cards.sort()

ssum = 0

for i in range(1,N):
    ssum = cards[i-1]+cards[i]
    cards[i] = ssum

ans = cards[-2]+ cards[-1]
print(ans)