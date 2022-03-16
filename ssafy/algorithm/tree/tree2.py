def pre_order(v):
    global last
    if v <= last:   # 마지막 정점번호 이내
        print(v)    # visit(v)
        pre_order(v*2)
        pre_order(v*2+1)
