# 점화식
# Ai = min(Ai-1, Ai/2, Ai/3, Ai/5) + 1

d = [0] * 30001

n = int(input())
for i in range(2,n+1):
    # 현재 수에서 1을 빼는 경우
    d[i] = d[i-1] + 1

    if i%2==0:
        d[i] = min(d[i],d[i//2]+1)
    if i%3==0:
        d[i] = min(d[i], d[i//3]+1)
    if i%5==0:
        d[i] = min(d[i], d[i//5]+1)

print(d[n])