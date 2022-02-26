# 200.0000000000
# 속력  = 거리/시간

T = int(input())
for tc in range(1,T+1):
    D, A, B, F = map(int, input().split())
    AtoB_time = D/(A+B) # A와 B가 만날때까지 걸리는 시간
    ans = F * AtoB_time
    print(f"#{tc} {ans:.10f}")