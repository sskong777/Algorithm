import sys
sys.stdin = open('input.txt', 'r')

def enq(n):
    global last
    last += 1
    tree[last] = n
    c = last
    p = c//2
    # 부모가 있고, 자식이 키 값이 더 작으면 교환
    while p >= 1 and tree[c] < tree[p]:
        tree[c], tree[p] = tree[p] , tree[c]
        c = p
        p = c//2

# 조상 구하기, 조상에 담겨있는 값 의 합 리턴
def find_anc(last_node):
    anc = []
    while last_node != 1:
        last_node //= 2
        anc.append(tree[last_node])
    return sum(anc)

T = int(input())
for tc in range(1,T+1):
    V = int(input())
    arr = list(map(int,input().split()))
    tree = [0]*(V+1)
    last = 0
    # 인큐
    for i in range(V):
        enq(arr[i])
    # print(tree)

    # 마자막 노드의 조상 구하기
    last_node = V
    print(f'#{tc} {find_anc(last_node)}')
