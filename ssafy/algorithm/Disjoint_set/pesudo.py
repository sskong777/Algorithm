# p: 노드 x 의 부모 저장
# rank: 루트 노드가 x 인 트리의 랭크값 저장
def Make_Set(x):
    p[x] = x
    rank[x] = 0


def Find_Set(x):
    if x == p[x]:
        return x
    else:
        return Find_Set(p[x])


def Union(x, y):
    # p[Find_Set(y) + Find_Set(x)]
    Link(Find_set(x), Find_set(y))


def Link(x, y):
    if rank[x] > rank[y]:
        p[y] = x
    else:
        p[x] = y

    if rank[x] == rank[y]:
        rank[y] += 1