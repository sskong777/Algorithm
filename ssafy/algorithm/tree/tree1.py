'''
4
1 2 1 3 3 4 3 5
'''
def pre_order(v):
    if v:
        print(v)
        pre_order(ch1[v])
        pre_order(ch2[v])

def in_order(v):
    if v:
        in_order(ch1[v])
        print(v)
        in_order(ch2[v])

def post_order(v):
    if v:
        post_order(ch1[v])
        post_order(ch2[v])
        print(v)


E = int(input())
arr = list(map(int,input().split()))
V = E + 1

ch1 = [0] * (V+1)
ch2 = [0] * (V+1)

for i in range(E):
    p,c = arr[i*2], arr[i*2+1]
    if ch1[p] == 0:
        ch1[p] = c
    else:
        ch2[p] = c

# 자식번호를 인덱스로 부모번호를 저장
par = [0] *(V+1)
for i in range(E):
    p,c = arr[i*2],arr[i*2+1]
    par[c] = p


# 루트 찾기에 사용.
root = 0
for i in range(1,V+1):
    if par[i] == 0:
        root = i

# 조상 찾기
c = 5   # 정점 c의 조상찾기
anc = []
while par[c] != 0:
    anc.append(par[c])
    c = par[c]
print('5의 조상: ', anc)


print('root: ',root)
print('par: ',par)
print('ch1: ',ch1)
print('ch2: ',ch2)
print('전위순회')
pre_order(3)
print('중위순회')
in_order(1)
print('후위순회')
post_order(3)