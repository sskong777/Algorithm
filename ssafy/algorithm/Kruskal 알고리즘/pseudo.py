def MST_KRUSKAL(G):
    mst = []

    for i in range(N):
        Make_Set(i)

    G.sort(key = lambda t:t[2]) # 가중치 기준으로 정렬
    mst_cost = 0 # MST 가중치

    while len(mst) < N-1:
        node_a, node_b, weight = G.pop(0) # 최소 가중치 간선 가져오기
        if Find_Set(node_a) != Find_Set(node_b): # 다른 집합인지 확인
            Union(node_a, node_b)
            mst.append((node_a, node_b)) # 트리에 (node_a, node_b) 추가
            mst_cost += weight