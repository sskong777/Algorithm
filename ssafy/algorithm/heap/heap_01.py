'''
최대ㅑ 100개의 정수
최대 힙
'''

def enq(n):
    global last
    last += 1
    tree[last] = n
    c = last    # 자식
    p = c // 2  # 부모 정점 번호
    while p >= 1 and tree[p] < tree[c]:
        # 부모가 있고, 자식의 키 값이 더 크면 교환
        tree[p], tree[c] = tree[c], tree[p]
        c = p
        p = c//2

def deq():
    global last
    tmp = tree[1]   # 루트의 key값
    tree[1] = tree[last]    # 마지막 정점의 키를 루트에 복사
    last -= 1       # 마지막 정점 삭제
    # 부모 > 자식 규칙 유지
    p = 1
    c = p * 2   # 왼쪽 자식 노드 번호
    while c <= last: # 왼쪽 자식이 있으면
        if c+1 <= last and tree[c] < tree[c+1]: # 오른쪽 자식노드도 있고 더 크면
            c += 1
        if tree[p] < tree[c]:   # 자식의 키 값이 더 크면 교환
            tree[p], tree[c] = tree[c], tree[p]
            p = c
            c = p * 2
        else:
            break
    return tmp



tree = [0] * 101
last = 0

enq(3)
enq(2)
enq(4)
enq(7)
enq(5)
enq(1)
# print(tree[1])
enq(9)
# print(tree[1])

while last > 0:
    print(deq(), tree[1])
