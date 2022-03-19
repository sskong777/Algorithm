import sys
sys.stdin = open('input.txt')

def calc(w, a, b):
    calc_dict = {
        '+': a + b,
        '-': a - b,
        '*': a * b,
        '/': a // b,
    }
    return calc_dict[w]

# 후위 순회
def postorder(node):
    res = 0
    if len(tree[node]) == 2:
        return tree[node][1]
    else:
        l = postorder(tree[node][2])
        # print('l',l)
        r = postorder(tree[node][3])
        # print('r',r)
        res = calc(tree[node][1], l, r)
        # print('res',res)
        return res

# 숫자만 형변환
def chg_number(char):
    if char.isnumeric():
        return int(char)
    else:
        return char



for tc in range(1, 11):
    N = int(input())      # 정점의 개수
    tree = [0]            # 앞에는 비워두고 인덱스 1부터 시작
    for _ in range(N):
        tree.append(list(map(chg_number, input().split())))
    res = postorder(1)
    print(f'#{tc} {res}')