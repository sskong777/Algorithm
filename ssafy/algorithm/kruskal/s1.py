import sys
sys.stdin = open('input.txt', 'r')


def find_set(x):
    # loop 활용
    while x != P[x]:
        x = P[x]
    return x

    # 재귀
    # if x == P[x]:
    #     return x
    # else:
    #     return find_set(P[x])

V, E = map(int, input().split())
edge = []
for _ in range(E):
    s, e, d = map(int, input().split())
    edge.append((d, s, e))   # 거리를 앞에 넣어서 sort 함수로 편하게 정렬가능
# 거리를 기준으로 오름차순
edge.sort()

P = [i for i in range(V+1)]  # 부모 원소 초기화
count = 0   # 선택된 정점의 수
total = 0   # 거리의 합

for d, s, e in edge:
    x = find_set(s)
    y = find_set(e)
    if x != y:       # 사이클을 형성하지 않음
        count += 1
        total += d
        P[y] = x     # 부모 원소를 갱신

        if count == V:
            break

print(total)